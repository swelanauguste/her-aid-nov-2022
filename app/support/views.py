import json
from decimal import Decimal

import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, TemplateView

from .forms import DonationCreateForm, VolunteerCreateForm
from .models import Donation, Volunteer

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


class VolunteerCreateView(CreateView):
    model = Volunteer
    form_class = VolunteerCreateForm


class VolunteerDetailView(DetailView):
    model = Volunteer


class VolunteerListView(ListView):
    model = Volunteer
    queryset = Volunteer.objects.filter(remain_anonymous=False)


class SupportView(TemplateView):
    stripe_balance = dict(stripe.Balance.retrieve())
    stripe_balance_int = int(stripe_balance["pending"][0]["amount"]) / 100
    extra_context = {"stripe_balance": stripe_balance_int}
    template_name = "support/support.html"


def donation_create_view(request):
    if request.method == "POST":
        form = DonationCreateForm(request.POST)
        if form.is_valid():
            donation = form.save()
            request.session["donation_id"] = donation.id
        return render(request, "support/donate_detail.html", {"object": donation})
    else:
        form = DonationCreateForm()
    return render(request, "support/donate_form.html", {"form": form})


class DonationDetailView(DetailView):
    model = Donation


def donation_process_view(request):
    donation_id = request.session.get("donation_id", None)
    donation = get_object_or_404(Donation, id=donation_id)
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "unit_amount": int(donation.amount * Decimal(100)),
                        "currency": "xcd",
                        "product_data": {
                            "name": donation.name,
                        },
                    },
                    "quantity": 1
                    # "currency": "usd",
                    # "customer_details": {
                    #     "name": donation.name,
                    #     # "customer_email": donation.email,
                    # },
                }
            ],
            mode="payment",
            customer_creation="always",
            success_url=request.build_absolute_uri(
                reverse("support:donation-completed")
            ),
            cancel_url=request.build_absolute_uri(
                reverse("support:donation-cancelled")
            ),
        )
        donation.check_out_id = checkout_session['id']
        donation.save()
        return redirect(checkout_session.url, code=303)
    return render(request, "support/process.html", locals())


def donation_completed(request):
    return render(request, "support/completed.html")


def donation_cancelled(request):
    return render(request, "support/cancelled.html")

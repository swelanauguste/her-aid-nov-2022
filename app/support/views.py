import stripe
from django.conf import settings
from django.shortcuts import redirect, render, reverse
from django.views import View

from .forms import DonationCreateForm
from .models import Donate

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION


def donation_create_view(request):
    if request.method == "POST":
        form = DonationCreateForm(request.POST)
        if form.is_valid():
            donation = form.save()
        return render(request, "support/donation_create.html", {"form": form})
    else:
        form = DonationCreateForm()
    return render(request, "support/donation_create.html", {"form": form})


def donation_completed(request):
    return render(request, "donation/completed.html")


def donation_cancelled(request):
    return render(request, "donation/cancelled.html")


class CreateStripeCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        donation = Donate.objects.get(id=self.kwargs["pk"])

        checkout_session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[
                {
                    "price_data": {
                        "currency": "xcd",
                        "unit_amount": int(donation.amt) * 100,
                        "donation_data": {
                            "name": donation.name,
                            "note": donation.note,
                        },
                    }
                }
            ],
            metadata={"donation_id": donation.id},
            mode="payment",
            success_url=request.build_absolute_uri(reverse("donation-completed")),
            cancel_url=request.build_absolute_uri(reverse("donation-cancelled")),
        )
        return redirect(checkout_session["url"])

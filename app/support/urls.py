from django.urls import path

from .views import (
    DonationDetailView,
    SupportView,
    VolunteerCreateView,
    VolunteerDetailView,
    VolunteerListView,
    donation_cancelled,
    donation_completed,
    donation_create_view,
    donation_process_view,
)
from .webhooks import stripe_webhook

app_name = "support"

urlpatterns = [
    path("", SupportView.as_view(), name="support"),
    path("volunteer-create", VolunteerCreateView.as_view(), name="volunteer-create"),
    path(
        "volunteer-list/",
        VolunteerListView.as_view(),
        name="volunteer-list",
    ),
    path(
        "volunteer-detail/<int:pk>/",
        VolunteerDetailView.as_view(),
        name="volunteer-detail",
    ),
    path(
        "donation-detail/<int:pk>/",
        DonationDetailView.as_view(),
        name="donation-detail",
    ),
    path("donation-create/", donation_create_view, name="donation-create"),
    path("donation-process/", donation_process_view, name="donation-process"),
    path("donation-cancelled/", donation_cancelled, name="donation-cancelled"),
    path("donation-completed/", donation_completed, name="donation-completed"),
    path("webhook/", stripe_webhook, name="stripe-webhook"),
]

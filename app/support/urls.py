from django.urls import path

from .views import (
    CreateStripeCheckoutSessionView,
    donation_cancelled,
    donation_completed,
    donation_create_view,
)

app_name = "support"

urlpatterns = [
    path("donation-create", donation_create_view, name="donation-create"),
    path("donation", CreateStripeCheckoutSessionView.as_view(), name="donation-stripe"),
    path("donation_cancelled", donation_cancelled, name="donation-cancelled"),
    path("donation_completed", donation_completed, name="donation-completed"),
]

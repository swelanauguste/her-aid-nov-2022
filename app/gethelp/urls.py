from django.urls import path

from . import views

app_name = "gethelp"

urlpatterns = [
    path("", views.Referral.as_view(), name="get-help"),
    path("app/", views.GetHelpViewMobile.as_view(), name="get-help-mobile"),
]

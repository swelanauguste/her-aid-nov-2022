from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("mobile/", views.MobileHome.as_view(), name="mobile-home"),
]

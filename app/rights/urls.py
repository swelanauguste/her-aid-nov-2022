from django.urls import path

from . import views

app_name = "rights"

urlpatterns = [
    path("", views.Right.as_view(), name='rights'),
]

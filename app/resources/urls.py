from django.urls import path

from . import views

app_name = "resources"

urlpatterns = [
    path("", views.Resource.as_view(), name="resources"),
    path(
        "detail/<int:pk>/", views.ResourceDetailView.as_view(), name="resource-detail"
    ),
]

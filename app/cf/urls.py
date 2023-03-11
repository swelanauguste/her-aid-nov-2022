from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("home.urls", namespace="home")),
    path("resources/", include("resources.urls", namespace="resources")),
    path("rights/", include("rights.urls", namespace="rights")),
    path("get-help/", include("gethelp.urls", namespace="gethelp")),
    path("support/", include("support.urls", namespace="support")),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

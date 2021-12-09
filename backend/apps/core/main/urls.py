from django.urls import include, path

from .views import MainRedirectView

urlpatterns = [
    path("", MainRedirectView.as_view()),
    path("api/", include("apps.core.api.urls"), name="api"),
]

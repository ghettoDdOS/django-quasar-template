from django.urls import include, path

app_name = "v1"

urlpatterns = [
    path("schedule/", include("apps.api.schedule.v1")),
    path("news/", include("apps.api.news.v1")),
]

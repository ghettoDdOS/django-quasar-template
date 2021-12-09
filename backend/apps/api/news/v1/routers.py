from django.urls import path

from .views import NewsDetail, NewsList

app_name = "news"

urlpatterns = [
    path("", NewsList.as_view()),
    path("<int:id_news>", NewsDetail.as_view()),
]

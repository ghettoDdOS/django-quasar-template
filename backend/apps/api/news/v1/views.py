from apps.api.news.models import News
from apps.api.news.v1.serializers import NewsSerializer
from rest_framework import generics, views
from rest_framework.pagination import PageNumberPagination


class NewsListSetPagination(PageNumberPagination):
    """
    Пагинация списка новостей
    """
    page_size = 5
    page_size_query_param = 'page_size'


class NewsList(generics.ListAPIView):
    """Список нововстей"""

    serializer_class = NewsSerializer
    pagination_class = NewsListSetPagination

    def get_queryset(self):
        queryset = News.objects.filter(is_published=True)
        return queryset


class NewsDetail(generics.RetrieveAPIView):
    """Получение одной новости"""

    lookup_url_kwarg = "id_news"
    serializer_class = NewsSerializer

    def get_queryset(self):
        id_news = self.kwargs["id_news"]
        queryset = News.objects.filter(id=id_news)
        return queryset

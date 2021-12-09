from apps.api.news.models import News, NewsImage
from rest_framework import serializers


class NewsImageSerializer(serializers.ModelSerializer):
    """
    Сериализатор изображений новостей
    """

    class Meta:
        model = NewsImage
        fields = [
            "id",
            "image",
        ]


class NewsSerializer(serializers.ModelSerializer):
    """
    Сериализатор новостей
    """

    images = NewsImageSerializer(many=True)

    date = serializers.DateTimeField(format="%d %B %Y")

    class Meta:
        model = News
        fields = "__all__"

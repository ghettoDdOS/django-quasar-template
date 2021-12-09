from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    """
    Новости
    """

    title = models.CharField(max_length=255, verbose_name=_("Анонс"))
    main_image = models.ImageField(null=False, blank=False, verbose_name=_("Фото"))
    text = models.TextField(null=True, blank=True, verbose_name=_("Текст"))
    date = models.DateTimeField(
        default=datetime.now, verbose_name=_("Дата публикации")
    )
    is_published = models.BooleanField(_("Опубликовано"), default=False)

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
        ordering = ["-date"]

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    """
    Изображение новости
    """

    news = models.ForeignKey(
        News, models.CASCADE, related_name="images", verbose_name=_("Новость")
    )
    image = models.ImageField(verbose_name=_("Изображение"))

    class Meta:
        verbose_name = _("Изображение новости")
        verbose_name_plural = _("Изображения новостей")

    def __str__(self):
        return str(_("Изображение"))

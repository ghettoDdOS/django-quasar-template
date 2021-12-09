from django.contrib import admin

from .models import News, NewsImage


class ImageInline(admin.TabularInline):
    model = NewsImage

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

@admin.register(NewsImage)
class NewsImageAdmin(admin.ModelAdmin):
    list_display = ("news", )

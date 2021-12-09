from django.contrib import admin

from . import models


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.FormOfEducation)
class FormOfEducationAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.LevelOfEducation)
class LevelOfEducationAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.SubGroup)
class SubGroupAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.KindSubject)
class KindSubjectAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.DayOfWeek)
class DayOfWeekAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.ParityWeek)
class ParityWeekAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(models.Chair)
class ChairAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.OrderLesson)
class OrderLessonAdmin(admin.ModelAdmin):
    list_display = (
        "public_id",
        "name",
    )


@admin.register(models.Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = (
        "file",
        "default_value",
        "date_time",
    )

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "teacher",
        "group",
        "level_of_education",
        "form_of_education",
        "subgroup",
        "subject",
        "kind",
        "day_of_week",
        "parity_week",
        "audience",
        "chair",
        "order_lesson",
    )
    list_filter = (
        "teacher",
        "group",
        "level_of_education",
        "form_of_education",
        "subject",
        "kind",
        "day_of_week",
        "parity_week",
        "audience",
        "chair",
        "order_lesson",
    )

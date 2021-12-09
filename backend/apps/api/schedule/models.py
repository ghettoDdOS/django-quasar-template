from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    """Преподаватель"""

    name = models.CharField(_("ФИО"), max_length=255)

    class Meta:
        verbose_name = _("Преподаватель")
        verbose_name_plural = _("Преподаватели")
        unique_together = [
            "name",
        ]

    def __str__(self):
        return self.name


class FormOfEducation(models.Model):
    """
    Форма обучения
    """

    public_id = models.IntegerField(_("ID"), blank=True)

    name = models.CharField(
        _("Наименование формы обучения"), max_length=255, blank=True
    )

    class Meta:
        verbose_name = _("Форма обучения")
        verbose_name_plural = _("Формы обучения")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class LevelOfEducation(models.Model):
    """
    Уровень образования
    """

    public_id = models.IntegerField(_("ID"))

    name = models.CharField(
        _("Наименование уровня образования"), max_length=255
    )

    class Meta:
        verbose_name = _("Уровень образования")
        verbose_name_plural = _("Уровни образования")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class Group(models.Model):
    """Группа"""

    name = models.CharField(_("Наименование группы"), max_length=255)

    class Meta:
        verbose_name = _("Группа")
        verbose_name_plural = _("Группы")
        unique_together = [
            "name",
        ]

    def __str__(self):
        return self.name


class SubGroup(models.Model):
    """Подгруппа"""

    public_id = models.IntegerField(_("ID"))

    name = models.CharField(_("Наименование"), max_length=255)

    class Meta:
        verbose_name = _("Подгруппа")
        verbose_name_plural = _("Подгруппа")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class KindSubject(models.Model):
    """Тип предмета"""

    name = models.CharField(_("Наименование типа"), max_length=255)

    class Meta:
        verbose_name = _("Тип предмета")
        verbose_name_plural = _("Тип предмета")
        unique_together = [
            "name",
        ]

    def __str__(self):
        return self.name


class Subject(models.Model):
    """Предмет"""

    name = models.CharField(_("Наименование предмета"), max_length=255)

    class Meta:
        verbose_name = _("Предмет")
        verbose_name_plural = _("Предмет")
        unique_together = [
            "name",
        ]

    def __str__(self):
        return self.name


class DayOfWeek(models.Model):
    """День недели"""

    public_id = models.IntegerField(_("ID"))

    name = models.CharField(_("Наименование дня"), max_length=255)

    class Meta:
        verbose_name = _("День недели")
        verbose_name_plural = _("День недели")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class ParityWeek(models.Model):
    """Четность недели"""

    public_id = models.IntegerField(_("ID"))

    name = models.CharField(_("Наименование четности"), max_length=255)

    class Meta:
        verbose_name = _("Четность недели")
        verbose_name_plural = _("Четность недели")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class Audience(models.Model):
    """Аудитория"""

    name = models.CharField(_("Номер аудитории"), max_length=255)

    class Meta:
        verbose_name = _("Аудитория")
        verbose_name_plural = _("Аудитория")
        unique_together = [
            "name",
        ]

    def __str__(self):
        return self.name


class Chair(models.Model):
    """Кафедра"""

    public_id = models.IntegerField(_("ID"))

    name = models.CharField(_("Наименование кафедры"), max_length=255)

    class Meta:
        verbose_name = _("Кафедра")
        verbose_name_plural = _("Кафедра")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class OrderLesson(models.Model):
    """Время занятия"""

    public_id = models.IntegerField(_("ID"))

    name = models.CharField(_("Время занятия"), max_length=255)

    class Meta:
        verbose_name = _("Время занятия")
        verbose_name_plural = _("Время занятия")
        unique_together = [
            "name",
            "public_id",
        ]

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """Пара"""

    teacher = models.ForeignKey(
        "schedule.Teacher",
        verbose_name=_("Преподаватель"),
        on_delete=models.CASCADE,
    )

    group = models.ForeignKey(
        "schedule.Group", verbose_name=_("Группа"), on_delete=models.CASCADE
    )

    form_of_education = models.ForeignKey(
        "schedule.FormOfEducation",
        verbose_name=_("Форма обучения"),
        on_delete=models.CASCADE,
    )

    level_of_education = models.ForeignKey(
        "schedule.LevelOfEducation",
        verbose_name=_("Уровень обучения"),
        on_delete=models.CASCADE,
    )

    subgroup = models.ForeignKey(
        "schedule.SubGroup",
        verbose_name=_("Подгруппа"),
        on_delete=models.CASCADE,
    )

    subject = models.ForeignKey(
        "schedule.Subject", verbose_name=_("Предмет"), on_delete=models.CASCADE
    )

    kind = models.ForeignKey(
        "schedule.KindSubject",
        verbose_name=_("Тип предмета"),
        on_delete=models.CASCADE,
    )

    day_of_week = models.ForeignKey(
        "schedule.DayOfWeek",
        verbose_name=_("День недели"),
        on_delete=models.CASCADE,
    )

    parity_week = models.ForeignKey(
        "schedule.ParityWeek",
        verbose_name=_("Четность недели"),
        on_delete=models.CASCADE,
    )

    audience = models.ForeignKey(
        "schedule.Audience",
        verbose_name=_("Аудитория"),
        on_delete=models.CASCADE,
    )

    chair = models.ForeignKey(
        "schedule.Chair", verbose_name=_("Кафедра"), on_delete=models.CASCADE
    )

    order_lesson = models.ForeignKey(
        "schedule.OrderLesson",
        verbose_name=_("Время занятия"),
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _("Пара")
        verbose_name_plural = _("Пары")

    def __str__(self):
        return f"{self.subject} {self.group}"


class Upload(models.Model):
    """Заполнение расписания"""

    file = models.FileField(
        _("Файл расписания"),
        upload_to="schedule/",
        max_length=100,
        null=True,
        help_text="Расписание обновится в течении 10 минут",
    )

    default_value = models.BooleanField(
        _("Заполнить статические значения"), default=False
    )

    date_time = models.DateTimeField(
        _("Время загрузки"),
        auto_now=False,
        auto_now_add=False,
        default=timezone.now,
    )

    class Meta:
        verbose_name = _("Файл расписания")
        verbose_name_plural = _("Файлы расписания")

    def __str__(self):
        return f"{self.file} {self.date_time}"

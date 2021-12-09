from apps.api.schedule.models import (
    Audience,
    Chair,
    DayOfWeek,
    FormOfEducation,
    Group,
    KindSubject,
    Lesson,
    LevelOfEducation,
    OrderLesson,
    ParityWeek,
    SubGroup,
    Subject,
    Teacher,
    Upload,
)
from rest_framework import serializers


class UploadSerializer(serializers.ModelSerializer):
    """
    Время наполнения
    """

    class Meta:
        model = Upload
        fields = "__all__"

class GroupSerializer(serializers.ModelSerializer):
    """
    Группы
    """

    class Meta:
        model = Group
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    """
    Преподаватели
    """

    class Meta:
        model = Teacher
        fields = "__all__"


class FormOfEducationSerializer(serializers.ModelSerializer):
    """
    Формы обучения
    """

    class Meta:
        model = FormOfEducation
        fields = "__all__"


class LevelOfEducationSerializer(serializers.ModelSerializer):
    """
    Уровни обучения
    """

    class Meta:
        model = LevelOfEducation
        fields = "__all__"


class SubGroupSerializer(serializers.ModelSerializer):
    """
    Подгруппы
    """

    class Meta:
        model = SubGroup
        fields = "__all__"


class KindSubjectSerializer(serializers.ModelSerializer):
    """
    Тип предмета
    """

    class Meta:
        model = KindSubject
        fields = "__all__"


class DayOfWeekSerializer(serializers.ModelSerializer):
    """
    День недели
    """

    class Meta:
        model = DayOfWeek
        fields = "__all__"


class ParityWeekSerializer(serializers.ModelSerializer):
    """
    Четность недели
    """

    class Meta:
        model = ParityWeek
        fields = "__all__"


class AudienceSerializer(serializers.ModelSerializer):
    """
    Аудитории
    """

    class Meta:
        model = Audience
        fields = "__all__"


class ChairSerializer(serializers.ModelSerializer):
    """
    Кафедра
    """

    class Meta:
        model = Chair
        fields = "__all__"


class OrderLessonSerializer(serializers.ModelSerializer):
    """
    Время занятия
    """

    start_time = serializers.SerializerMethodField("get_start_time")
    end_time = serializers.SerializerMethodField("get_end_time")

    class Meta:
        model = OrderLesson
        fields = ("id", "public_id", "start_time", "end_time")

    def get_start_time(self, obj):
        return obj.name.split(" - ")[0]

    def get_end_time(self, obj):
        return obj.name.split(" - ")[1]


class SubjectSerializer(serializers.ModelSerializer):
    """
    Предмет
    """

    class Meta:
        model = Subject
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    """
    Расписание для определенной группы
    """

    teacher = TeacherSerializer()
    form_of_education = FormOfEducationSerializer()
    level_of_education = LevelOfEducationSerializer()
    subgroup = SubGroupSerializer()
    subject = SubjectSerializer()
    kind = KindSubjectSerializer()
    day_of_week = DayOfWeekSerializer()
    parity_week = ParityWeekSerializer()
    audience = AudienceSerializer()
    chair = ChairSerializer()
    order_lesson = OrderLessonSerializer()
    group = GroupSerializer()

    class Meta:
        model = Lesson
        fields = "__all__"

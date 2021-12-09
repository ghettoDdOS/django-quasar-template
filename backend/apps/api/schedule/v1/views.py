from apps.api.schedule.models import Group, Lesson, Teacher, Upload
from apps.api.schedule.services import ChangeOfItemTypeName
from rest_framework import generics

from ..v1.serializers import (
    GroupSerializer,
    LessonSerializer,
    TeacherSerializer,
    UploadSerializer,
)


class GroupList(generics.ListAPIView):
    """Список всех групп"""

    serializer_class = GroupSerializer

    def get_queryset(self):
        queryset = Group.objects.all()
        return queryset

class UploadList(generics.ListAPIView):
    """Список всех дат наполнений"""

    serializer_class = UploadSerializer

    def get_queryset(self):
        queryset = Upload.objects.all()
        return queryset


class LessonList(generics.ListAPIView):
    """Список расписания для группы"""

    lookup_url_kwarg = "group"
    serializer_class = LessonSerializer

    def get_queryset(self):
        group = self.kwargs["group"]
        queryset = Lesson.objects.filter(group=group)
        for item in queryset:
            item.kind.name = ChangeOfItemTypeName.execute(
                {"name_kind_lesson": item.kind.name}
            )
        return queryset


class TeacherList(generics.ListAPIView):
    """Список всех преподавателей"""

    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.all()
        return queryset


class TeachersLessonList(generics.ListAPIView):
    """Список пар для определенного преподавателя"""

    lookup_url_kwarg = "teacher"
    serializer_class = LessonSerializer

    def get_queryset(self):
        teacher = self.kwargs["teacher"]
        queryset = Lesson.objects.filter(teacher=teacher)
        for item in queryset:
            item.kind.name = ChangeOfItemTypeName.execute(
                {"name_kind_lesson": item.kind.name}
            )
        return queryset

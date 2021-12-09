from django.urls import path

from .views import (
    GroupList,
    LessonList,
    TeacherList,
    TeachersLessonList,
    UploadList,
)

app_name = "schedule"

urlpatterns = [
    path("groups", GroupList.as_view()),
    path("teachers", TeacherList.as_view()),
    path("lessons/group/<int:group>", LessonList.as_view()),
    path("lessons/teacher/<int:teacher>", TeachersLessonList.as_view()),
    path("upload", UploadList.as_view()),
]

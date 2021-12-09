import csv
import os

from apps.api.schedule import constants, models


class BaseScheduleParser:

    base_path = ""
    schedule_data = csv.DictReader

    def get_schedule_data(self, file):
        csv_file = open(
            os.path.join(self.base_path, file), "r", encoding="utf8"
        )
        self.schedule_data = csv.DictReader(csv_file, delimiter=";")

    def import_in_schedule(self):
        """
        Наполнение главной таблицы
        """
        try:
            models.Lesson.objects.bulk_create(
                [
                    models.Lesson(
                        teacher=models.Teacher.objects.get_or_create(
                            name=row["Name"]
                        )[0],
                        group=models.Group.objects.get_or_create(
                            name=row["Group"]
                        )[0],
                        subgroup=models.SubGroup.objects.get(
                            public_id=row["Subg"]
                        ),
                        subject=models.Subject.objects.get_or_create(
                            name=row["Subject"]
                        )[0],
                        kind=models.KindSubject.objects.get_or_create(
                            name=row["Subj_type"]
                        )[0],
                        day_of_week=models.DayOfWeek.objects.get(
                            public_id=row["Day"]
                        ),
                        parity_week=models.ParityWeek.objects.get(
                            public_id=row["Week"]
                        ),
                        audience=models.Audience.objects.get_or_create(
                            name=row["Aud"]
                        )[0],
                        chair=models.Chair.objects.get_or_create(
                            public_id=row["CafID"]
                        )[0],
                        order_lesson=models.OrderLesson.objects.get(
                            public_id=row["Les"]
                        ),
                        form_of_education=models.FormOfEducation.objects.get(
                            public_id=0
                        ),
                        level_of_education=models.LevelOfEducation.objects.get(
                            public_id=0
                        ),
                    )
                    for row in self.schedule_data
                ]
            )
        except Exception as e:
            print(e)
            print("Модель 'Пары' уже наполнена")

    def default_values(self):
        """
        Наполнение таблиц статическими значениями
        """

        try:
            models.SubGroup.objects.bulk_create(
                [
                    models.SubGroup(public_id=value[0], name=value[1])
                    for value in constants.SUB_GROUP
                ]
            )
        except Exception:
            print("Модель 'Подгруппа' уже наполнена статическими значениями")

        try:
            models.FormOfEducation.objects.bulk_create(
                [
                    models.FormOfEducation(public_id=value[0], name=value[1])
                    for value in constants.FORM_OF_EDUCATION
                ]
            )
        except Exception:
            print(
                "Модель 'Форма обучения' уже наполнена статическими значениями"
            )

        try:
            models.LevelOfEducation.objects.bulk_create(
                [
                    models.LevelOfEducation(public_id=value[0], name=value[1])
                    for value in constants.LEVEL_OF_EDUCATION
                ]
            )
        except Exception:
            print(
                """
                Модель 'Уровень обучения' уже наполнена статическими значениями
                """
            )

        try:
            models.OrderLesson.objects.bulk_create(
                [
                    models.OrderLesson(public_id=value[0], name=value[1])
                    for value in constants.ORDER_LESSON
                ]
            )
        except Exception:
            print(
                "Модель 'Время занятия' уже наполнена статическими значениями"
            )

        try:
            models.DayOfWeek.objects.bulk_create(
                [
                    models.DayOfWeek(public_id=value[0], name=value[1])
                    for value in constants.DAY_OF_WEEK
                ]
            )
        except Exception:
            print("Модель 'День недели' уже наполнена статическими значениями")

        try:
            models.ParityWeek.objects.bulk_create(
                [
                    models.ParityWeek(public_id=value[0], name=value[1])
                    for value in constants.PARITY_WEEK
                ]
            )
        except Exception:
            print(
                """
                Модель 'Четность недели' уже наполнена статическими значениями
                """
            )


class UploadedFileParser(BaseScheduleParser):
    def __init__(self, file, default_value=False):
        if default_value:
            self.default_values()
        self.get_schedule_data(file)
        self.import_in_schedule()

from apps.api.schedule import models


class ClearSchedule:

    main_models = [
        models.Audience,
        models.Chair,
        models.Teacher,
        models.Group,
        models.KindSubject,
        models.Lesson,
        models.Subject,
    ]

    default_values_models = [
        models.SubGroup,
        models.FormOfEducation,
        models.LevelOfEducation,
        models.OrderLesson,
        models.DayOfWeek,
        models.ParityWeek,
    ]

    def __init__(self, default_value=False):
        models = self.main_models
        if default_value:
            models += self.default_values_models
        self.clear(models)

    def clear(self, models):
        for model in models:
            model.objects.all().delete()

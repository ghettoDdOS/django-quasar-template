from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ScheduleConfig(AppConfig):
    """Default app config"""

    name = "apps.api.schedule"
    verbose_name = _("Расписание")

    def ready(self):
        from . import signals  # noqa: F401 # pylint: disable=unused-import

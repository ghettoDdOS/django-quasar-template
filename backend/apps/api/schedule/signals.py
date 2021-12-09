from threading import Thread

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Upload
from .services import ClearSchedule, UploadedFileParser


def init_file_processing(instance):
    ClearSchedule(default_value=instance.default_value)
    UploadedFileParser(
        file=instance.file._get_file().name,
        default_value=instance.default_value,
    )


@receiver(post_save, sender=Upload)
def post_save_file(sender, instance, created, **kwargs):

    if created:
        Thread(target=init_file_processing, args=(instance,)).start()

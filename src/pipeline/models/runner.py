from uuid import uuid4
from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string


def make_secret_key():
    return get_random_string(length=32)


class Runner(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    addr = models.URLField(max_length=255)
    key = models.CharField(
        max_length=32,
        editable=False,
        default=make_secret_key
    )
    alive = models.BooleanField(default=True)
    last_update = models.DateTimeField(default=timezone.now)

    class Meta(object):
        ordering = ['name']

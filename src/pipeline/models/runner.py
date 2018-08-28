from uuid import uuid4
from django.db import models
from django.utils import timezone


class Runner(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    addr = models.URLField(max_length=255)
    alive = models.BooleanField(default=True)
    last_update = models.DateTimeField(default=timezone.now)

    class Meta(object):
        ordering = ['name']

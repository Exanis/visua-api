from uuid import uuid4
from django.db import models


class Pipeline(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)

    class Meta(object):
        ordering = ['name']

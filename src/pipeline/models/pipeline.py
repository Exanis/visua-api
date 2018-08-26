from uuid import uuid4
from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class Pipeline(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    model = JSONField(default='')

    class Meta(object):
        ordering = ['name']

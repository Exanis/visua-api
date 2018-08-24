from uuid import uuid4
from django.db import models
from django.contrib.postgres.fields.jsonb import JSONField


class Block(models.Model):
    uuid = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255)
    data = JSONField()

    class Meta(object):
        ordering = ['name']

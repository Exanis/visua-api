"""
User model. Superset the usual user to use an uuid instead of an id.
"""

from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class User(AbstractUser):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False
    )
    secret_key = models.CharField(
        max_length=32,
        default=get_random_string(length=32)
    )

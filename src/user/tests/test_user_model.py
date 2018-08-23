"""
Testing user model
Mostly test that user model is the default one
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from user.models import User


class UserTestCase(TestCase):
    @staticmethod
    def test_user_model_subclass_user():
        assert issubclass(User, AbstractUser)

    @staticmethod
    def test_default_user_model_is_this_app():
        user = get_user_model()()
        assert isinstance(user, User)

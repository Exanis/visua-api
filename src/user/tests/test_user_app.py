from django.test import TestCase
from user.apps import UserConfig
import user


class UserAppTestCase(TestCase):
    @staticmethod
    def test_user_app_label():
        user_app = UserConfig('user', user)
        assert user_app.name == 'user'

from django.test import TestCase
from pipeline.apps import PipelineConfig
import pipeline


class UserAppTestCase(TestCase):
    @staticmethod
    def test_user_app_label():
        user_app = PipelineConfig('pipeline', pipeline)
        assert user_app.name == 'pipeline'

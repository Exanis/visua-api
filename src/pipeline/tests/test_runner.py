from django.conf import settings
from rest_framework.test import APITestCase
from user.models import User
from pipeline import models


class RunnerTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('test', password='test')
        cls.target = models.Runner.objects.create(name='test', addr='http://test.com')

    def _login(self):
        self.client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })

    def test_create(self):
        self._login()
        result = self.client.post('/api/project/runner/', {
            'name': 'test',
            'addr': 'http://test.com'
        })
        self.assertEqual(result.status_code, 403)
        result = self.client.post('/api/project/runner/', {
            'name': 'test',
            'addr': 'http://test.com',
            'token': settings.RUNNER_KEY
        })
        self.assertEqual(result.status_code, 201)

    def test_update(self):
        self._login()
        result = self.client.put('/api/project/runner/' + str(self.target.uuid) + '/', {'name': 'test', 'addr': 'http://test.net'})
        self.assertEqual(result.status_code, 405)

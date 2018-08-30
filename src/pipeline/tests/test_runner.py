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
        self.assertIn('key', result.data)

    def test_update(self):
        self._login()
        result = self.client.put('/api/project/runner/' + str(self.target.uuid) + '/', {'name': 'test', 'addr': 'http://test.net'})
        self.assertEqual(result.status_code, 405)

    def test_single(self):
        self._login()
        result = self.client.get('/api/project/runner/' + str(self.target.uuid) + '/')
        self.assertEqual(result.status_code, 200)
        self.assertNotIn('key', result.data)

    def test_token(self):
        self._login()
        result = self.client.get('/api/project/runner/token/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('token', result.data)
        self.assertEqual(result.data['token'], settings.RUNNER_KEY)

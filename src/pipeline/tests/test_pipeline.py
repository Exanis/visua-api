from rest_framework.test import APITestCase
from user.models import User
from pipeline import models


class PipelineTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('test', password='test')
        models.Pipeline.objects.create(name='test')

    def _login(self):
        self.client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })

    def test_list(self):
        self._login()
        result = self.client.get('/api/project/pipeline/')
        self.assertEqual(result.status_code, 200)
        self.assertNotIn('model', result.data['results'][0])

    def test_single(self):
        self._login()
        uuid = models.Pipeline.objects.get().uuid
        result = self.client.get('/api/project/pipeline/' + str(uuid) + '/')
        self.assertEqual(result.status_code, 200)
        self.assertIn('model', result.data)

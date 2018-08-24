from json import dumps
from user.models import User
from pipeline import models
from rest_framework.test import APIClient, APITestCase


class BlockDataTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('test', password='test')

    def _login(self):
        self.client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })

    def test_correct_data(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'dataInput': [],
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 201)
        self.assertEqual(models.Block.objects.get().name, 'test')

    def test_bad_version(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '2',
                    'name': 'test',
                    'dataInput': [],
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_version(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'name': 'test',
                    'dataInput': [],
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_name(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'dataInput': [],
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_empty_name(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': '',
                    'dataInput': [],
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_long_name(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'a' * 256,
                    'dataInput': [],
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_data_input(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_bad_data_input(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'dataInput': 'test',
                    'dataOutput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_data_output(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'dataInput': [],
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_bad_data_output(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'dataInput': [],
                    'dataOutput': 'test',
                    'varsInput': [],
                    'varsOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_vars_input(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'varsOutput': [],
                    'dataInput': [],
                    'dataOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_bad_vars_input(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'varsInput': 'test',
                    'varsOutput': [],
                    'dataInput': [],
                    'dataOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_vars_output(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'varsInput': [],
                    'dataInput': [],
                    'dataOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_bad_vars_output(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'varsInput': [],
                    'varsOutput': 'test',
                    'dataInput': [],
                    'dataOutput': [],
                    'image': 'some/docker:image'
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_no_image(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'varsInput': [],
                    'varsOutput': [],
                    'dataInput': [],
                    'dataOutput': []
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

    def test_empty_image(self):
        self._login()
        result = self.client.post(
            '/api/project/block/',
            {
                'data': dumps({
                    'apiVersion': '1',
                    'name': 'test',
                    'varsInput': [],
                    'varsOutput': [],
                    'dataInput': [],
                    'dataOutput': [],
                    'image': ''
                })
            }
        )
        self.assertEqual(result.status_code, 400)
        self.assertEqual(models.Block.objects.count(), 0)

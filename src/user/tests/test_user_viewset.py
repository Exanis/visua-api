from user import models
from django.test import TestCase
from rest_framework.test import APIClient


class UserTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.User.objects.create_user('test', password='test')
        models.User.objects.create_user('test2', password='test')

    @staticmethod
    def test_user_login():
        client = APIClient()
        result = client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'bad_password'
        })
        assert result.status_code == 400
        result = client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        assert result.status_code == 200

    @staticmethod
    def test_user_refresh_token():
        client = APIClient()
        client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        result = client.post('/api/user/auth/refresh/')
        assert result.status_code == 200

    @staticmethod
    def test_user_logout():
        client = APIClient()
        client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        result = client.post('/api/user/logout/')
        assert result.status_code == 204
        result = client.get('/api/user/me/')
        assert result.status_code == 401

    @staticmethod
    def test_user_me():
        client = APIClient()
        client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        result = client.get('/api/user/me/')
        assert result.status_code == 200
        assert result.data['username'] == 'test'

    @staticmethod
    def test_user_permission():
        client = APIClient()
        client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        target = models.User.objects.get(username='test2')
        me = models.User.objects.get(username='test')
        result = client.get('/api/user/' + me.uuid.hex + '/')
        assert result.status_code == 200
        result = client.get('/api/user/' + target.uuid.hex + '/')
        assert result.status_code == 403

    @staticmethod
    def test_user_update_password():
        client = APIClient()
        client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        me = models.User.objects.get(username='test')
        result = client.patch('/api/user/' + me.uuid.hex + '/', {
            'password': '12345678'
        })
        assert result.status_code == 400
        result = client.patch('/api/user/' + me.uuid.hex + '/', {
            'password': 'a good password'
        })
        assert result.status_code == 200
        result = client.patch('/api/user/' + me.uuid.hex + '/', {
            'first_name': 'testing'
        })
        assert result.status_code == 200
        me.is_staff = True
        me.save()
        client.post('/api/user/auth/login/', {
            'username': 'test',
            'password': 'test'
        })
        result = client.post('/api/user/', {
            'first_name': 'some',
            'last_name': 'thing',
            'email': 'an@email.it',
            'password': '12345678',
            'username': 'something'
        })
        assert result.status_code == 400
        result = client.post('/api/user/', {
            'first_name': 'some',
            'last_name': 'thing',
            'email': 'an@email.it',
            'password': 'something good as a password !',
            'username': 'something'
        })
        assert result.status_code == 201

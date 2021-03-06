from user import viewsets
from django.urls import include, path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token


ROUTER = routers.DefaultRouter()
ROUTER.register('', viewsets.User)


urlpatterns = [
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh/', viewsets.REFRESH_JWT_TOKEN),
    path('', include(ROUTER.urls))
]

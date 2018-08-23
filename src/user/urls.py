from django.urls import include, path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from user import viewsets


router = routers.DefaultRouter()
router.register('', viewsets.User)


urlpatterns = [
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
    path('', include(router.urls))
]

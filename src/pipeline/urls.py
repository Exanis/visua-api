from django.urls import include, path
from rest_framework import routers
from pipeline import viewsets


ROUTER = routers.DefaultRouter()
ROUTER.register('', viewsets.Pipeline)


urlpatterns = [
    path('', include(ROUTER.urls))
]

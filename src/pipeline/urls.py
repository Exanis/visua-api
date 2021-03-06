from django.urls import include, path
from rest_framework import routers
from pipeline import viewsets


ROUTER = routers.DefaultRouter()
ROUTER.register('pipeline', viewsets.Pipeline)
ROUTER.register('block', viewsets.Block)
ROUTER.register('runner', viewsets.Runner)


urlpatterns = [
    path('', include(ROUTER.urls))
]

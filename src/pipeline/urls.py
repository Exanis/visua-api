from django.urls import include, path
from rest_framework import routers
from pipeline import viewsets


router = routers.DefaultRouter()
router.register('', viewsets.Pipeline)


urlpatterns = [
    path('', include(router.urls))
]

from django.conf import settings
from rest_framework import viewsets, filters, permissions, response, status
from pipeline import serializers, models


class Runner(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = models.Runner.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Runner

    def create(self, request, *args, **kwargs):
        if 'token' not in request.data or request.data['token'] != settings.RUNNER_KEY:
            return response.Response(status=status.HTTP_403_FORBIDDEN)
        return super(Runner, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return response.Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

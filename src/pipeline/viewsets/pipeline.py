from rest_framework import viewsets, filters, permissions
from pipeline import serializers, models


class Pipeline(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = models.Pipeline.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    serializer_class = serializers.Pipeline
    permission_classes = [permissions.IsAuthenticated]

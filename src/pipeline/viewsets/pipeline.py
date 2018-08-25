from rest_framework import viewsets, filters, permissions
from pipeline import serializers, models


class Pipeline(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = models.Pipeline.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.Pipeline
        return serializers.FullPipeline

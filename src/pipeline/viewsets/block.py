from rest_framework import viewsets, filters, permissions
from pipeline import serializers, models


class Block(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = models.Block.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Block

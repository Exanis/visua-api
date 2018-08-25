from rest_framework import viewsets, filters, permissions, decorators, response
from pipeline import serializers, models


class Block(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = models.Block.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ('name',)
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Block

    @decorators.action(methods=['GET'], detail=False)
    def all(self, request):
        data = self.get_serializer(self.get_queryset(), many=True)
        return response.Response(data=data.data)

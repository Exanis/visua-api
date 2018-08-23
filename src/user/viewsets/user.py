from django.conf import settings
from rest_framework import viewsets, decorators, response, status, filters
from user import serializers, models, permissions


class User(viewsets.ModelViewSet):
    lookup_field = 'uuid'
    queryset = models.User.objects.all()
    permission_classes = [permissions.User]
    filter_backends = [filters.SearchFilter]
    search_fields = ('username', 'first_name', 'last_name', 'email')

    def get_serializer_class(self):
        if self.request.user.is_staff:
            return serializers.AdminUser
        return serializers.User

    @decorators.action(methods=['GET'], detail=False)
    def me(self, request):
        serialized = self.get_serializer(request.user)
        return response.Response(data=serialized.data)

    @decorators.action(methods=['POST'], detail=False)
    def logout(self, request):
        ret = response.Response(status=status.HTTP_204_NO_CONTENT)
        ret.delete_cookie(settings.JWT_AUTH['JWT_AUTH_COOKIE'])
        return ret

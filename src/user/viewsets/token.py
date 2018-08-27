from rest_framework import serializers
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.serializers import RefreshJSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings


class RefreshCookieJSONWebTokenSerializer(RefreshJSONWebTokenSerializer):
    token = serializers.CharField(required=False)

    def validate(self, attrs):
        attrs['token'] = self.context['request'].COOKIES.get(api_settings.JWT_AUTH_COOKIE)
        return super(RefreshCookieJSONWebTokenSerializer, self).validate(attrs)


class RefreshCookeJSONWebToken(JSONWebTokenAPIView):
    serializer_class = RefreshCookieJSONWebTokenSerializer


refresh_jwt_token = RefreshCookeJSONWebToken.as_view()

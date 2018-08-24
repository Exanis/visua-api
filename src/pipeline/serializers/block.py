import json
from rest_framework import serializers
from pipeline import models


ACCEPTED_VERSIONS = ['1']


class Block(serializers.ModelSerializer):
    uuid = serializers.UUIDField(
        read_only=True
    )

    data = serializers.JSONField(
        required=True,
        allow_null=False,
        error_messages={
            'required': 'errorMissingData',
            'null': 'errorMissingData',
            'invalid': 'errorInvalidData',
        }
    )

    @staticmethod
    def _error(error):
        raise serializers.ValidationError({
            'data': error
        })

    # Note: Not covering some lines here because when testing, DRF check json first and decode it,
    # but when the server is actually running, it does not so we need to decode it ourselves
    # Also for some reasons pylint is not seeing a member of json class ?
    def validate(self, attrs):
        data = attrs['data']
        if isinstance(data, str):  # pragma: no cover
            try:  # pragma: no cover
                data = json.loads(data)  # pragma: no cover
            except json.JSONDecodeError:  # pragma: no cover pylint: disable=no-member
                Block._error('errorInvalidData')  # pragma: no cover
        if 'apiVersion' not in data:
            Block._error('errorMissingApiVersion')
        if data['apiVersion'] not in ACCEPTED_VERSIONS:
            Block._error('errorInvalidVersion')
        if 'name' not in data or not data['name']:
            Block._error('errorMissingName')
        if len(data['name']) > 255:
            Block._error('errorNameTooLong')
        if 'dataInput' not in data:
            Block._error('errorMissingDataInput')
        if not isinstance(data['dataInput'], list):
            Block._error('errorInvalidDataInput')
        if 'dataOutput' not in data:
            Block._error('errorMissingDataOutput')
        if not isinstance(data['dataOutput'], list):
            Block._error('errorInvalidDataOutput')
        if 'varsInput' not in data:
            Block._error('errorMissingVarsInput')
        if not isinstance(data['varsInput'], list):
            Block._error('errorInvalidVarsInput')
        if 'varsOutput' not in data:
            Block._error('errorMissingVarsOutput')
        if not isinstance(data['varsOutput'], list):
            Block._error('errorInvalidVarsOutput')
        if 'image' not in data or not data['image']:
            Block._error('errorMissingImage')
        attrs['name'] = data['name']
        return attrs

    class Meta(object):
        model = models.Block
        fields = [
            'uuid',
            'name',
            'data'
        ]

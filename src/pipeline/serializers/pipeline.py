from rest_framework import serializers, validators
from pipeline.models import Pipeline as PipelineModel


class Pipeline(serializers.ModelSerializer):
    uuid = serializers.UUIDField(
        read_only=True
    )
    name = serializers.CharField(
        min_length=2,
        max_length=255,
        required=True,
        allow_null=False,
        allow_blank=False,
        validators=[
            validators.UniqueValidator(
                queryset=PipelineModel.objects.all(),
                message='errorPipelineNameExists'
            )
        ],
        error_messages={
            'invalid': 'errorPipelineNameRequired',
            'blank': 'errorPipelineNameRequired',
            'required': 'errorPipelineNameRequired',
            'null': 'errorPipelineNameRequired',
            'max_length': 'errorPipelineNameTooLong',
            'min_length': 'errorPipelineNameTooShort',
        }
    )

    class Meta(object):
        model = PipelineModel
        fields = [
            'uuid',
            'name'
        ]

from rest_framework import serializers
from pipeline import models


class Runner(serializers.ModelSerializer):
    class Meta(object):
        model = models.Runner
        fields = [
            'uuid',
            'name',
            'addr',
            'alive',
            'last_update'
        ]
        read_only_fields = [
            'uuid',
            'last_update',
            'alive'
        ]


class RunnerWithKey(Runner):
    class Meta(Runner.Meta):
        fields = Runner.Meta.fields + ['key']
        read_only_fields = Runner.Meta.fields + ['key']

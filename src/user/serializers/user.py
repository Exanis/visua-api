from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from rest_framework import serializers, validators
from user.models import User as UserModel


class User(serializers.ModelSerializer):
    uuid = serializers.UUIDField(
        read_only=True
    )
    username = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        min_length=2,
        max_length=150,
        validators=[
            validators.UniqueValidator(
                queryset=UserModel.objects.all(),
                message='errorUsernameExists'
            )
        ],
        error_messages={
            'invalid': 'errorUsernameRequired',
            'blank': 'errorUsernameRequired',
            'required': 'errorUsernameRequired',
            'null': 'errorUsernameRequired',
            'max_length': 'errorUsernameTooLong',
            'min_length': 'errorUsernameTooShort',
        }
    )
    first_name = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        min_length=2,
        max_length=30,
        error_messages={
            'invalid': 'errorFirstNameRequired',
            'blank': 'errorFirstNameRequired',
            'required': 'errorFirstNameRequired',
            'null': 'errorFirstNameRequired',
            'max_length': 'errorFirstNameTooLong',
            'min_length': 'errorFirstNameTooShort',
        }
    )
    last_name = serializers.CharField(
        required=True,
        allow_null=False,
        allow_blank=False,
        min_length=2,
        max_length=150,
        error_messages={
            'invalid': 'errorLastNameRequired',
            'blank': 'errorLastNameRequired',
            'required': 'errorLastNameRequired',
            'null': 'errorLastNameRequired',
            'max_length': 'errorLastNameTooLong',
            'min_length': 'errorLastNameTooShort',
        }
    )
    email = serializers.EmailField(
        required=True,
        allow_null=False,
        allow_blank=False,
        validators=[
            validators.UniqueValidator(
                queryset=UserModel.objects.all(),
                message='errorEmailExists'
            )
        ],
        error_messages={
            'invalid': 'errorEmailInvalid',
            'blank': 'errorEmailRequired',
            'required': 'errorEmailRequired',
            'null': 'errorEmailRequired',
        }
    )
    password = serializers.CharField(
        required=False,
        allow_null=False,
        allow_blank=False,
        min_length=2,
        max_length=150,
        write_only=True,
        error_messages={
            'invalid': 'errorPasswordInvalid',
            'blank': 'errorPasswordInvalid',
            'null': 'errorPasswordInvalid',
            'max_length': 'errorPasswordTooLong',
            'min_length': 'errorPasswordTooShort',
        }
    )
    
    def validate(self, data):
        user = self.instance
        if user is None:
            user = UserModel(**data)

        if 'password' in data:
            try:
                validate_password(data.get('password'), user=user)
                data['password'] = make_password(data['password'])
            except ValidationError as e:
                raise serializers.ValidationError({
                    'password': list(e.messages)
                })
        return super(User, self).validate(data)

    class Meta(object):
        model = UserModel
        fields = [
            'uuid',
            'username',
            'first_name',
            'last_name',
            'password',
            'email'
        ]


class AdminUser(User):
    is_staff = serializers.BooleanField(required=False, default=False)
    
    class Meta(User.Meta):
        fields = User.Meta.fields + ['is_staff']

from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer, Serializer

from reviews.models import User


class SignUpSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email')

    @staticmethod
    def validate_username(value):
        if value == 'me':
            raise ValidationError(
                'Использовать имя "me" в качестве username запрещено.'
            )
        return value


class UserSerializer(SignUpSerializer):

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )


class ProfileSerializer(SignUpSerializer):
    role = StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )


class TokenSerializer(Serializer):
    username = CharField()
    confirmation_code = CharField()

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')

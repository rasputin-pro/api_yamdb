from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.relations import SlugRelatedField, StringRelatedField
from rest_framework.serializers import ModelSerializer, Serializer, IntegerField

from reviews.models import User, Category, Genre, Title


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


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug',)


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug',)


class TitleReadSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    rating = IntegerField(read_only=True)

    class Meta:
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )
        model = Title


class TitleWriteSerializer(ModelSerializer):
    category = SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug'
    )
    genre = SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True
    )

    class Meta:
        fields = (
            'id', 'name', 'year', 'description', 'genre', 'category'
        )
        model = Title

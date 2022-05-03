from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = (
    ('user', 'Пользователь'),
    ('moderator', 'Модератор'),
    ('admin', 'Администратор'),
)


class User(AbstractUser):
    email = models.EmailField(
        unique=True,
        verbose_name='email'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    role = models.CharField(
        max_length=255,
        choices=ROLE_CHOICES,
        default='user',
        verbose_name='Роль пользователя'
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username

    @property
    def is_user(self):
        return self.role == 'user'

    @property
    def is_moderator(self):
        return self.role == 'moderator'

    @property
    def is_admin(self):
        return self.role == 'admin'


class Category (models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='название категории')    
    slug = models.SlugField(
        unique=True,
        verbose_name='слаг категории')
    
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name
    

class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='название жанра')
    slug = models.SlugField(
        max_length=50,
        unique=True,
        verbose_name='slug')

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(
        max_length=128,
        verbose_name='название')
    year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        verbose_name='год выпуска',
    )
    description = models.TextField(
        blank=True,
        verbose_name='описание'
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        blank=True,
        verbose_name='жанр'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        blank=True,
        null=True,
        verbose_name='категория'
    )

    class Meta:
        verbose_name = 'произведение'
        verbose_name_plural = 'произведения'

    def __str__(self):
        return self.name
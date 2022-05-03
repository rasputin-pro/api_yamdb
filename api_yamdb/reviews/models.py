from datetime import datetime

from operator import mod
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator



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
    name = models.TextField(
        verbose_name='название категории'
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        verbose_name='слаг категории'
    )

class Genre(models.Model):
    name = models.TextField(
        verbose_name='название жанра'
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        verbose_name='слаг жанра'
    )

class Title(models.Model):
    name = models.TextField(
        verbose_name='названиие произведения'
    )
    year = models.IntegerField(
        verbose_name='год выпуска',
        null=True
    )
    description = models.TextField(
        verbose_name='Описание')
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='жанр произведения'
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='категория произведения'
    )
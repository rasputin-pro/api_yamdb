# Generated by Django 2.2.16 on 2022-05-03 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220502_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Название Категории')),
                ('slug', models.SlugField(unique=True, verbose_name='слаг категории')),
            ],
        ),
    ]

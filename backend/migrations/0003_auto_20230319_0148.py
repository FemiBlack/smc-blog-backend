# Generated by Django 3.2.18 on 2023-03-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=5500, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=5500, unique=True, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(max_length=5500, unique=True, verbose_name='Slug'),
        ),
    ]
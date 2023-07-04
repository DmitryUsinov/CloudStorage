# Generated by Django 4.2.2 on 2023-06-29 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Storage', '0005_remove_file_discipline_id_file_discipline_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='file',
            name='slug',
            field=models.SlugField(blank=True, max_length=150, unique=True),
        ),
    ]
# Generated by Django 4.2.10 on 2024-02-21 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_reviewrating_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewrating',
            name='movie_title',
        ),
    ]

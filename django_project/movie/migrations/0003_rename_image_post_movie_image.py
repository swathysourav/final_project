# Generated by Django 4.2.10 on 2024-02-18 13:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='movie_image',
        ),
    ]

# Generated by Django 4.2.10 on 2024-02-21 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_reviewrating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.2.5 on 2021-11-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torrents', '0002_auto_20211114_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=255, unique=True),
        ),
    ]

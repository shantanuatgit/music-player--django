# Generated by Django 2.2.13 on 2021-01-14 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boom', '0010_auto_20210114_1242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='song',
        ),
    ]

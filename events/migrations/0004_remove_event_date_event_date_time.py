# Generated by Django 5.1.3 on 2024-12-06 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AddField(
            model_name='event',
            name='date_time',
            field=models.DateTimeField(default='2024-12-06 00:00'),
            preserve_default=False,
        ),
    ]

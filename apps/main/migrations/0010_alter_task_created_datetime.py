# Generated by Django 5.1.5 on 2025-01-27 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_task_created_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 6, 34, 56, 960128, tzinfo=datetime.timezone.utc)),
        ),
    ]

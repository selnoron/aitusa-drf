# Generated by Django 5.1.5 on 2025-01-26 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_task_created_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_datetime',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 26, 20, 31, 27, 422640, tzinfo=datetime.timezone.utc)),
        ),
    ]

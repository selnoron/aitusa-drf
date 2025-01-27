from django.db import models
import datetime
from django.utils import timezone 


class Task(models.Model):
    title = models.CharField(
        verbose_name='titleOfTask',
        unique=True,
        max_length=20
    )
    text = models.CharField(
        verbose_name="task's_text",
        null=True,
        max_length=400
    )
    is_updated = models.BooleanField(
        verbose_name="is_updated?",
        default=False
    )
    is_completed = models.BooleanField(
        verbose_name="is_completed?",
        default=False
    )
    created_datetime = models.DateTimeField(
        default=timezone.now()
    )
    is_deleted = models.BooleanField(
        verbose_name="is_deleted?",
        default=False
    )
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

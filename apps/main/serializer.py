from rest_framework import serializers
from main.models import Task


class TaskSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    title = serializers.CharField()
    text = serializers.CharField()
    is_updated = serializers.BooleanField()
    is_completed = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    created_datetime = serializers.DateTimeField()


class TaskCreateSerializer(serializers.ModelSerializer):
    created_datetime = serializers.DateTimeField(format="%d.%m.%Y %H:%M")

    class Meta:
        model = Task
        fields = ['pk', 'title', 'text', 'is_updated', 'is_completed', 'is_deleted', 'created_datetime']


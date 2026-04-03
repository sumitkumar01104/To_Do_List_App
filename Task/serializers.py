from rest_framework import serializers
from .models import Task, Subtask


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Subtask
        fields = ['id', 'title', 'status', 'is_completed', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)

    class Meta:
        model  = Task
        fields = [
            'id', 'title', 'subject', 'due_date',
            'status', 'is_completed', 'subtasks', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
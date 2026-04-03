from django.contrib import admin
from .models import Task, Subtask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display  = ['title', 'user', 'subject', 'due_date', 'status', 'is_completed', 'created_at']
    list_filter   = ['status', 'is_completed', 'subject']
    search_fields = ['title', 'user__username']


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display  = ['title', 'task', 'status', 'is_completed', 'created_at']
    list_filter   = ['status', 'is_completed']
    search_fields = ['title', 'task__title']
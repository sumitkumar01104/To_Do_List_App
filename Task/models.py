from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title       = models.CharField(max_length=255)
    subject     = models.CharField(max_length=100, blank=True, null=True)
    due_date    = models.DateField(blank=True, null=True)
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    is_completed = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} — {self.title}"


class Subtask(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('done', 'Done'),
    ]

    task         = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='subtasks')
    title        = models.CharField(max_length=255)
    status       = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    is_completed = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"{self.task.title} → {self.title}"
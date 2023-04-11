from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)
    descreption = models.TextField(default='', blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_add = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self) -> str:
        return self.task


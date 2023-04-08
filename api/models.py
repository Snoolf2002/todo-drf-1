from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=100)
    descreption = models.TextField(default='', blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_add = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.task

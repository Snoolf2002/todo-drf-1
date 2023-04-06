from rest_framework import serializers
from .models import Todo

class TodoSerialzier(serializers.Serializer):
    task = serializers.CharField(max_length=100)
    descreption = serializers.CharField()
    completed = serializers.BooleanField()
    created_add = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
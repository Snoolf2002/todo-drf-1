from rest_framework import serializers
from .models import Todo

class TodoSerialzier(serializers.Serializer):
    task = serializers.CharField(max_length=100)
    descreption = serializers.CharField()
    completed = serializers.BooleanField()
    # created_add = serializers.DateTimeField()
    # updated_at = serializers.DateTimeField()

    def create(self, validate_data):
        todo = Todo.objects.create(
            task = validate_data["task"],
            descreption = validate_data["descreption"],
            completed = validate_data["completed"]
        )
        return todo
    
    def update(self, instance, validated_data):
        # if validated_data.get('task') is not None:
        #     instance.task = validated_data["task"]
        # if validated_data.get('descreption') is not None:
        #     instance.descreption = validated_data["descreption"]
        # if validated_data.get('completed') is not None:
        #     instance.completed = validated_data["completed"]

        instance.task = validated_data["task"]
        instance.descreption = validated_data["descreption"]
        instance.completed = validated_data["completed"]
        instance.save()
        
        return instance
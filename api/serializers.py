from rest_framework import serializers
from .models import Todo

# class TodoSerialzier(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     task = serializers.CharField(max_length=100)
#     descreption = serializers.CharField(allow_blank=True)
#     completed = serializers.BooleanField(default=False)
#     # created_add = serializers.DateTimeField()
#     # updated_at = serializers.DateTimeField()

#     def to_representation(self, instance):
#         return {
#             "id": instance.id,
#             "title": instance.task,
#             "descreption": instance.descreption,
#             "status": instance.completed
#         }

#     def create(self, validate_data):
#         todo = Todo.objects.create(
#             task = validate_data["task"],
#             descreption = validate_data["descreption"],
#             completed = validate_data["completed"]
#         )
#         return todo
    
#     def update(self, instance, validated_data):
#         instance.task = validated_data.get('task', instance.task)
#         instance.descreption = validated_data.get('descreption', instance.descreption)
#         instance.completed = validated_data.get('completed', instance.completed)
#         instance.save()
        
#         return instance


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task', 'descreption', 'completed', 'student']


        
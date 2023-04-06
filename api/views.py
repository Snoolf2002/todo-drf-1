from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerialzier
# Create your views here.


class TodoApiView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        data = {
            "results": []
        }
        for todo in todos:
            serializer = TodoSerialzier(todo)
            data["results"].append(
                serializer.data
                # {
                #     "task": todo.task,
                #     "descreption": todo.descreption,
                #     "completed": todo.completed,
                #     "created_add": todo.created_add,
                #     "updated_at": todo.updated_at
                # }
            )
        
        return Response(data)
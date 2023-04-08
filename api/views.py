from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Todo
from .serializers import TodoSerialzier
# Create your views here.


class TodoApiView(APIView):
    def get(self, request: Request) -> Response:
        todos = Todo.objects.all()
        serializer = TodoSerialzier(todos, many=True)
        data = {
            "results": serializer.data
        }
        return Response(data)
    
    def post(self, request: Request) -> Response:
        serializer = TodoSerialzier(data=request.data)

        if serializer.is_valid():
            data = serializer.save()
            print(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['POST'])
def update_task(request, id):
    print(type(request))
    if request.method == "POST":
        try:
            todo = Todo.objects.get(id=id)
        except:
            data = {
                "status": "object doesn't exist"
            }
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        
        serializer = TodoSerialzier(instance=todo, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"status": "you must send POST request"})
    
@api_view(["GET"])
def delete_task(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        data = {
            "status": "object doesn't exist"
        }
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    
    todo.delete()
    serializer = TodoSerialzier(todo)
    return Response(serializer.data)
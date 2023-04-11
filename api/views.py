from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.http import JsonResponse

from .models import Todo, User
from .serializers import TodoSerializer


class TodoApiView(APIView):
    def get(self, request: Request, id=None) -> Response:
        if id is None:
            todos = Todo.objects.all()
            serializer = TodoSerializer(todos, many=True)
            data = {
                "results": serializer.data
            }
            return Response(data)
        else:
            try:
                todo = Todo.objects.get(id=id)
            except:
                return JsonResponse({"status": "object doesn't exist"})
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = TodoSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request: Request, id):
        try:
            todo = Todo.objects.get(id=id)
        except:
            return JsonResponse({"status": "object doesn't exist"})
        
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, id):
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            todo.delete()
        except:
            return JsonResponse({"status": "object doesn't exist"})
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
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
        
        serializer = TodoSerializer(instance=todo, data=request.data)

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
    serializer = TodoSerializer(todo)
    return Response(serializer.data)


class UserView(APIView):
    def get(self, request: Request, user) -> Response:
        try:
            student = User.objects.get(username__icontains=user)
        except:
            return JsonResponse({"status": "user doesn't exist"})
        
        todos = Todo.objects.filter(student=student)
        serializer = TodoSerializer(todos, many=True)

        return Response(serializer.data)
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializers import TodoSerializer

# method_1

@api_view(['GET', 'POST'])
def todo_list_create(request):

    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','DELETE','PUT'])
def todo_detail(request, id):

    todo = get_object_or_404(Todo, id=id)

    if request.method == 'GET':
        # todo = Todo.objects.get(id=id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = TodoSerializer(data=request.data, instance=todo)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'deleted successfully'})

# method_2

class Todos(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # lookup_field = 'id'

# method_3

class TodoMVS(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


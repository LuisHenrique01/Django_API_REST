from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializers

@api_view(['GET'])
def todo_list(request):
    if request.methond == 'GET':
        todo = Todo.objects.all()
        serializer = TodoSerializers(todo, many=True)
        return Response(serializer.data)
    elif request.methond == 'POST':
        serializer = TodoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
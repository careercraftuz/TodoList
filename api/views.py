from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Todo
from .serializers import TaskSerializer, UserSerializer
class TaskView(APIView):
    '''get all tasks'''
    def get(self, request: Request) -> Response:    
        tasks = Todo.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        data = serializer.data
        return Response(data)
    def post(self, request: Request) -> Response:
        '''add task'''
        data = request.data
        serialzer = TaskSerializer(data=data)
        if serialzer.is_valid():
            Todo.objects.get()
                
            serialzer.save()
            return Response(serialzer.data)
        
        return Response(serialzer.errors)
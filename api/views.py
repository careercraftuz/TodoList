from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from .models import Task

@api_view(["GET"])
def get_all_tasks(request:Request):
    if request.method == "GET":
        tasks=Task.objects.all()
        result={'result':[]}
        for task in tasks:
            result['result'].append({
                'id':task.id,
                'name':task.name,
                'description':task.description,
                'status':task.status,
                'created':task.created,
                'updated':task.updated
            })
        return Response(result)
    else:
        return Response({'result':'Wrong method'})

@api_view(['GET'])
def get_task(request,id:int):
    if request.method == 'GET':
        try:
            task=Task.objects.get(id=id)
            result={'result':[]}
            result['result'].append({
                'id':task.id,
                'name':task.name,
                'description':task.description,
                'status':task.status,
                'created':task.created,
                'updated':task.updated
            })
            return Response(result)
        except:
            return Response({'result':'Task not found'})
        
@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        try:
            task=request.data
            object=Task.objects.create(
                name=task['name'],
                description=task['description'],
                status=task['status']
            )
            object.save()
            return Response({'result':'created'},status=status.HTTP_201_CREATED)
        except:
            return Response({'result':'bad request'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'result':'Wrong method'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
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

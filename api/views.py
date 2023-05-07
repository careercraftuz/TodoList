from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from .models import Task
from rest_framework.authtoken.models import Token
from django.contrib import auth


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


class Get_task(APIView):   
    def GET(request:Request, id:int):
            user= request.user
            try:
                task=Task.objects.filter(user=user,id=id)
                result={
                    'id':task.id,
                    'name':task.name,
                    'description':task.description,
                    'status':task.status,
                    'created':task.created,
                    'updated':task.updated
                }
                return Response(result)
            except:
                return Response({'result':'Task not found'})


@api_view(['POST'])
def delete_task(request, id:int):
    if request.method == 'POST':
        try:
            task=Task.objects.get(id=id)
            task.delete()
            return Response({'result':'Task deleted'})
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
        except Exception as e:
            return Response({'result':f'bad request {e}'},status=status.HTTP_400_BAD_REQUEST)
    return Response({'result':'Wrong method'},status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def update_task(request,id:int):
    if request.method == 'POST':
        try:
            task = Task.objects.get(id=id)
            try:
                data=request.data
                task.name = data.get('name',task.name)
                task.description = data.get('description',task.description)
                task.status = data.get('status',task.status)

                task.save()
                return Response({'result':'Task updated'},status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'result':f'Bad request {e}'},status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'result':'Not found task'},status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'result':'Wrong method'},status=status.HTTP_405_METHOD_NOT_ALLOWED)
class LoginUser(APIView):
    def put(self,request:Request)->Response:
        user = request.user
        if user:
            token = Token.objects.get(user=user)
            token.delete()
            create_token=Token.objects.create(user=user)
            return Response({"new_token":create_token.key},status=status.HTTP_201_CREATED)
class Logoutuser(APIView):
    def delete(self,request:Request)->Response:
        user=request.user
        if user:
            token = Token.objects.get(user=user)
            token.delete()
            auth.logout(request)
            data={
                "result":"you logged out"
            }
            return Response(data=data, status=status.HTTP_200_OK)


from django.urls import path 
from .views import (
    get_all_tasks,
    Get_task,
    DeleteTask,
    UpdateTask,
    CreateTask,
    LoginUser,
    Logoutuser
)

urlpatterns = [
    path('tasks/', get_all_tasks),
    path('tasks/<int:id>',Get_task.as_view()),
    path('tasks/delete/<int:id>/', DeleteTask.as_view()),
    path('tasks/update/<int:id>/', UpdateTask.as_view()),
    path('createtask/',CreateTask.as_view()),
    path('new-token/',LoginUser.as_view()),
    path('logout/',Logoutuser.as_view()),

]


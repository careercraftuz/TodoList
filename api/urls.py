
from django.urls import path 
from .views import (
    get_all_tasks,
    Get_task,
    delete_task,
    update_task,
    CreateTask,
    LoginUser,
    Logoutuser
)

urlpatterns = [
    path('tasks/', get_all_tasks),
    path('tasks/<int:id>',Get_task.as_view()),
    path('tasks/<int:id>/delete', delete_task),
    path('tasks/<int:id>/update', update_task),
    path('createtask/',CreateTask.as_view()),
    path('new-token/',LoginUser.as_view()),
    path('logout/',Logoutuser.as_view()),

]


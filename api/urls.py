
from django.urls import path
from .views import (
    delete_task,
    update_task,
    create_token,
    Login,
    UserTasks,
    UserCreateTask,
    Logout,
    UserTasks,
    UserTaskid
)

urlpatterns = [
    path('tasks/<int:id>', UserTaskid.as_view()),
    path('tasks/<int:id>/delete', delete_task),
    path('tasks/<int:id>/update', update_task),
    path('create-task/',UserCreateTask.as_view()),
    path('register/',create_token),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('tasks/',UserTasks.as_view()),
]

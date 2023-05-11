
from django.urls import path
from .views import (
    TaskDetailView,
    delete_task,
    UpdateTasks,
    create_token,
    Login,
    UserTasks,
    UserCreateTask,
    Logout,
    UserTasks,
)

urlpatterns = [
    path('tasks/<int:id>', TaskDetailView.as_view()),
    path('tasks/<int:id>/delete', delete_task),
    path('tasks/<int:id>/update', UpdateTasks.as_view()),
    path('create-task/',UserCreateTask.as_view()),
    path('register/',create_token),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('tasks/',UserTasks.as_view()),
]

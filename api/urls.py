
from django.urls import path
from .views import (
    get_task,
    delete_task,
    update_task,
    create_task,
    create_token,
    Login,
    Logout,
    UserTasks,
)

urlpatterns = [
    path('tasks/<int:id>', get_task),
    path('tasks/<int:id>/delete', delete_task),
    path('tasks/<int:id>/update', update_task),
    path('create-task/',create_task),
    path('register/',create_token),
    path('login/',Login.as_view()),
    path('logout/',Logout.as_view()),
    path('tasks/',UserTasks.as_view()),
]

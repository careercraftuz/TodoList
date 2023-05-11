
from django.urls import path
from .views import (
    get_all_tasks,
    get_task,
    delete_task,
    LoginUser,
    update_task,
    create_task,
    create_token,
    Logoutuser,
)

urlpatterns = [
    path('tasks/', get_all_tasks),
    path('tasks/<int:id>', get_task),
    path('tasks/<int:id>/delete', delete_task),
    path('tasks/<int:id>/update', update_task),
    path('create-task/',create_task),
    path('token/', create_token, name='token'),
    path('new-token/',LoginUser.as_view()),
    path('logout/',Logoutuser.as_view()),
]

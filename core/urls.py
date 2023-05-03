
from django.contrib import admin
from django.urls import path
from api.views import (
    get_all_tasks,
    get_task,
    delete_task,
    update_task
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_all_tasks),
    path('tasks/<int:id>', get_task),
    path('tasks/<int:id>/delete', delete_task),
    path('tasks/<int:id>/update', update_task)
]

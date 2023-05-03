
from django.contrib import admin
from django.urls import path
from api.views import (
    get_all_tasks,
    get_task
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_all_tasks),
    path('task/<int:id>', get_task)
]

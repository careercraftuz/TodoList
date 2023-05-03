
from django.contrib import admin
from django.urls import path
from api.views import get_all_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', get_all_tasks)
]

from django.urls import path
from .views import TaskView,UserView,DeletTodo,UserCompletad,UserinCompletad,CreateUserview


urlpatterns = [
    path('all', TaskView.as_view()),
    path('task/<int:pk>', TaskView.as_view()),
]
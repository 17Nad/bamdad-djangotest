from django.urls import path
from todo_list.views import *


urlpatterns = [
    path('home/', home),
    path('tasks/', tasks_list)
]
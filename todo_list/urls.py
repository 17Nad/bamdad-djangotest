from django.urls import path
from todo_list.views import *


urlpatterns = [
    path('home/', home),
    path('tasks/', tasks_list),
    path("students_tasks/<int:st>/", students_tasks),
    path("mark_tasks/<int:id>/", mark_tasks)
]
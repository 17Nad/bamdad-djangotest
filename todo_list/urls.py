from django.urls import path
from todo_list.views import home


urlpatterns = [
    path('home/', home)
]
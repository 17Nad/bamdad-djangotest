from django.urls import path
from students.views import *


urlpatterns = [
    path('students/', students),
    path('top_students/', top_students)

]
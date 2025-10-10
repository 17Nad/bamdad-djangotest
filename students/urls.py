from django.urls import path
from students.views import *


urlpatterns = [
    path('all_students/', all_students),
    # path('top_students/', top_students)

]
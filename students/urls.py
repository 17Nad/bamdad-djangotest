from django.urls import path
from students.views import *

app_name = "students"
urlpatterns = [
    path('all_students/', all_students),
    #path('top_students/', top_students),
    path('add_student/', new_student),
    path ('courses/', courses_view),
    path("student_form/", student_form, name="student_form" ),
    path('student_dashboard/', student_dashboard, name="studentDashboard")
]
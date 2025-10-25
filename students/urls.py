from django.urls import path
from students.views import *

app_name = "students"
urlpatterns = [
    path('all_students/', all_students),
    path('top_students/<int:min_grade>', top_students),
    path('add_student/', new_student),
    path ('courses/', all_courses),
    path("student_form/", student_form, name="studentForm" ),
    path('student_dashboard/', student_dashboard, name="studentDashboard"),
    path ('courses/', all_courses),
    path('select_courses/<int:id>', select_courses),
    path('student_courses/<int:id>', student_courses)

]
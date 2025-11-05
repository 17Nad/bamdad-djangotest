from django.urls import path
from students.views import *
from students.viewss import *

app_name = "students"
urlpatterns = [
    path('all_students/', all_students),
    path('top_students/<int:min_grade>', top_students),
    path('add_student/', new_student),
    path ('courses/', all_courses),
    path("student_form/", student_form, name="studentForm" ),
    path('student_dashboard/', student_dashboard, name="studentDashboard"),
    path ("new_student_form/", StudentForm.as_view()),
    path('select_courses/<int:id>', select_courses),
    path('student_courses/<int:id>', student_courses),
    path('new_course/', CreateCourse.as_view, name="newCourse"),
    path('all_teachers/', TeacherView.as_view() ) 
]
from django.urls import path, include
from students.views import *
from students.viewss import *
from students.api import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"get-students", GetStudentsViewSet, basename="getStudents")
router.register(r"get-courses", GetCoursesViewSet, basename="getCourses")
router.register(r"get-teachers", GetTeachersViewSet, basename="getTeachers")
router.register(r"get-profiles", GetProfilesViewSet, basename="getProfiles")

app_name = "students"
urlpatterns = [
    path('all_students/', all_students),
    #path('top_students/<int:min_grade>', top_students),
    # path('add_student/', new_student),
    path ('courses/', CoursesView.as_view()),
    path ('courses/register/<int:cid>/', RegisterInCourse.as_view(), name="registerInCourse"),
    #path("student_form/", student_form, name="studentForm" ),
    path('student_dashboard/', student_dashboard, name="studentDashboard"),
    path ("new_student_form/", CreateStudent.as_view()),
    #path('courses/<int:cid>', select_courses), #TODO: create the view for this
    # path('student_courses/<int:id>', student_courses),
    path('courses/new-course', CreateCourse.as_view(), name="newCourse"),
    path('all_teachers/', TeacherView.as_view() ) ,
    #_________________________________________________api urls_______________________________________________________________
    path('api/students/', DisplayStudentAPIView.as_view(), name = 'allStudents'),
    path('api/students/<int:sid>', DisplayStudentAPIView.as_view()),
    path('api/courses/', DisplayCourseAPIView.as_view(), name = 'allCourses'),
    path('api/courses/<int:cid>', DisplayCourseAPIView.as_view()),
    path('api/courses/enroll/', EnrollCourseAPIView.as_view()),
    path('api/profile/<int:pid>', ProfileAPIView.as_view()),
    path('api/', include(router.urls)),
]
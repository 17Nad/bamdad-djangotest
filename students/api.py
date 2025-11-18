from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from students.models import *

class DisplayAllStudentsAPIView(APIView):
    def get(self, request):
        list = Profile.objects.filter(is_teacher=False).values_list(flat=True)
        return Response(request, {"names" : list})

class DisplayStudentDetailsAPIView(APIView):
    def get(self, request, sid):
        details = get_object_or_404(Student, id=sid).values_list("major", "grade" ,flat=True) #TODO: wtf?
        return Response(request, {"student" : details})
    
class DisplayAllCoursesAPIView(APIView):
    def get(self, request):
        list = Course.objects.all().values_list("title", flat=True)
        return Response(request, {"cources" : list})

class DisplayCourseDetailsAPIView(APIView):
    def get(self, request, cid):
        details = get_object_or_404(Course, id=cid).values_list(flat=True)
        return Response(request, {"details" : details})
    
class EnrollCourse(APIView, LoginRequiredMixin):
    def post(self, request, cid):
        user = request.user
        course = get_object_or_404(Course, id = cid)
        if course.is_active:
            try:
                course.students.add(user.profile.student)
                return Response (request, {"message": "registration successful!"})
            except user.profile.student.DoesNotExist:
                return Response (request, {"message": "You need to be a student to attend a course!"})
        else:
            raise PermissionDenied("This course is nolonger active. ") #TODO: why does it give me warning?
        
class ProfileAPIView(APIView, LoginRequiredMixin):
    def get(self, request, pid):
        profile = get_object_or_404(Profile, id=pid)
        details = profile.values_list("name", "bio", "phone_number", "birthday", "is_teacher", flat=True)
        return Response(request, {"profile": details})



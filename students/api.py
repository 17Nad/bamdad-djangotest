from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from students.models import *
from students.serializers import *


class DisplayStudentAPIView(APIView):
    def get(self, request, sid = None):
        if sid:
            student = get_object_or_404(Student, id=sid)
            details = {"name" : student.user.name,
                       "major" : student.major,
                       "grade" : student.grade}
            return Response(details, status=status.HTTP_200_OK)
        else:
            list = Profile.objects.filter(is_teacher=False).values_list("name",flat=True)
            return Response({"names" : list}, status=status.HTTP_200_OK)
        

class DisplayCourseAPIView(APIView):
    def get(self, request, cid=None):
        if cid:
            course = get_object_or_404(Course, id=cid)
            details = {
                "course": course.title,
                "description": course.description,
                "start": course.start,
                "end": course.end,
                "teacher": course.teacher.user.name
            }
            return Response({"details" : details}, status=status.HTTP_200_OK)
        else:
            list = Course.objects.all().values_list("title", flat=True)
            return Response({"cources" : list}, status=status.HTTP_200_OK)

    
class EnrollCourseAPIView(APIView): 

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    @csrf_exempt #too good for me yet :D
    def post(self, request):
        #user = request.user
        data = request.data
        course = Course.objects.get(id = data["cid"])
        student = Student.objects.get(id= data["sid"])
        if course.is_active:
            if not course.students.get(id = data["sid"]).exists(): 
                try:
                    course.students.add(student) #if student exists in our table, it will be added to the course. if it doesn't exist, it means we got a None from 'student' in line 52 which means 'sid' was invalid, or the user is a teacher.
                    return Response ({"message": "registration successful!"}, status = status.HTTP_200_OK)
                except student.DoesNotExist:
                    return Response ({"message": "You need to be a student to attend a course!"}, status = status.HTTP_406_NOT_ACCEPTABLE)
                except course.DoesNotExist:
                    return Response({"message": "This course doesn't exist"}, status = status.HTTP_404_NOT_FOUND)
            else: return Response({"message": "You are already a member of this course."}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"message":"This course is nolonger active. "} , status=status.HTTP_403_FORBIDDEN) 
        

class ProfileAPIView(APIView): #قبلش اینجا LoginRequiredMixin گذاشته بودم ولی ولش فعلا با مسائل مربوط به auth کاری نداریم 
    def get(self, request, pid):
        profile = Profile.objects.filter(id=pid) 
        details = profile.values("name", "bio", "phone_number", "birthday", "is_teacher")[0] #لیست میاره، بعد از لیست درش میاره خخخخخخ
        return Response(details, status= status.HTTP_200_OK)


#______________________________________________ViewSets & ModelViewSets_____________________________________________

class GetStudentsViewSet(ModelViewSet): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # def list(self, request):
    #     pass

    # def retrieve(self,request, pk):
    #     pass

class GetCoursesViewSet(ModelViewSet): 
    queryset = Course.objects.all()
    serializer_class = CoureSerializer


class GetTeachersViewSet(ModelViewSet): 
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class GetProfilesViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

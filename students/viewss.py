from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from django.views import View

class CreateStudent(View): 
    
    studentFormPage = "students/index9.html"

    def get (self, request):
        context = {"form" : StudentForm}
        return render(request, self.studentFormPage, context)
    
    def post(self, request):
        info = request.POST
        Student.objects.create(name = info["name"], field = info["field"], phone_number=info["phone_number"])
        context = { 
                   "message" : "your information has been successfully saved on the database!",
                    "info" : request.POST
        }
        return redirect ("students:studentDashboard")
    
class CoursesView(View):
    template = 'students/courses_view.html'
    def get(self, request):
        list = Course.objects.all()
        return render(self.request, self.template, {"cources": list})
    
class CourseDetails(View): #TODO: no template yet 
    template = 'students/course_details.html'
    def get(self, request, cid):
        course = Course.objects.get_object_or_404(id = cid)
        return render(request, self.template, {"course": course})        
        
class RegisterInCourse(View, LoginRequiredMixin):
    def post (self, request, cid):
        user = request.user
        course = Course.objects.get(id = cid)
        if course.is_active:
            try:
                course.students.add(user.profile.student)
                return redirect ("students:coursesView")
            except user.profile.student.DoesNotExist:
                return HttpResponseForbidden("<h1>403: Access Denied</h1><p>You must be a student to register in a course!</p>")
            except Course.DoesNotExist:
                return Http404("<h1>404: Not Found</h1><p>The course you are trying to register in does not exist!</p>")
            except:
                return HttpResponse("something went wrong.") 
        else:
            return HttpResponse("<h1>403: Access Denied</h1><p>This course is nolonger active.</p>")
    
    
class CreateCourse(View, LoginRequiredMixin):
    courseFormPage = "students/create_course.html"
    
    def get(self, request):
        return render(request, self.courseFormPage, {"form": CourseForm})
    
    def post(self, request):
        user = request.user
        try:            
            new = Course.objects.create(
                title=request.POST["title"],
                description=request.POST["description"],
                start=request.POST["start"],
                end=request.POST["end"] ,
                teacher = user.profile.teacher )
            context = {
                    "form": CourseForm,
                    "message0": "Course created successfully!\n If you want to create another course, please fill the form."}
        except ValueError:
            context = {
                    "form": CourseForm,
                    "message1": "Invalid date format. Please enter dates in this format: YYYY-MM-DD" }
        except user.profile.teacher.DoesNotExist:
                return HttpResponseForbidden("<h1>403: Access Denied </h1><p>You must be a teacher to create a course!</p>")
        return render(request, self.courseFormPage, context)

    
class TeacherView(View):
    def get(self, request):
        context = { "all" : Teacher.objects.all()}
        return render(request, "index10.html" , context)
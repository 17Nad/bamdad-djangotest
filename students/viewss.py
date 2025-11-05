from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.views import View

class StudentForm(View): 
    
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
    
    
class CreateCourse(View):
    courseFormPage = "students/index8.html"
    
    def get(self, request):
        return render(self.request, self.courseFormPage, {"form": CourseForm})
    
    def post(self, request):
        try:            
            new = Course.objects.create(
                title=request.POST["title"],
                description=request.POST["description"],
                start=request.POST["start"],
                end=request.POST["end"] )
            context = {
                "form": CourseForm,
                "message0": "Course created successfully!\n If you want to create another course, please fill the form."}
        except ValueError:
            context = {
                "form": CourseForm,
                "message1": "Invalid date format. Please enter dates in this format: YYYY-MM-DD" }
        return render(self.request, self.courseFormPage, context)
    
class TeacherView(View):
    def get(self, request):
        context = { "all" : Teacher.objects.all()}
        return render(request, "index10.html" , context)
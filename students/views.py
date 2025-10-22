from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StudentForm
 
def all_students(request):
    context = {"all": Student.objects.all()}
    return render(request, 'students/index.html', context)

# def top_students(request):
#     context = {"top": list(Student.objects.filter(grade__gte=80))}
#     return render(request, 'students/index.html', context)

def new_student(request):
    Student.objects.create("new", "ea", 0)
    new = all_students(request)
    return new #??????????????????????

# def students_tasks(request):
#     context = {"tasks": Student.objects.filter(id=1)}
#     return render(request, 'students/index3.html', context)

def courses_view(request):
    context = { "all" : Course.objects.all()}
    return render(request, 'students/index4.html', context)

def student_form(request):
    studentFormPage = "students/index7.html"
    if request.method == "GET":
        context = {"form" : StudentForm}
        return render(request, studentFormPage, context)
    elif request.method == "POST":
        info = request.POST
        Student.objects.create(name = info["name"], field = info["field"], phone_number=info["phone_number"])
        context = { 
                   "message" : "your information has been successfully saved on the database!",
                    "info" : request.POST
        }
        return redirect ("students:studentDashboard")
    
def student_dashboard(request):
    return HttpResponse("this is your dashboard")
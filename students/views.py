from django.shortcuts import render
from django.http import HttpResponse
from .models import *


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
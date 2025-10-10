from django.shortcuts import render
from django.http import HttpResponse
from .models import Student


def all_students(request):
    context = {"all": Student.objects.all()}
    return render(request, 'students/index.html', context)

# def top_students(request):
#     context = {"top": list(Student.objects.filter(grade__gte=80))}
#     return render(request, 'students/index.html', context)

def new_student(request):
    new = Student.objects.create("new", "ea", 00 )
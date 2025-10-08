from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def students(request):
    list = Student.objects.all()
    return HttpResponse(list)

def top_students(request):
    list = Student.objects.filter(grade__gte=80)
    return HttpResponse(list)
from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def length_check(name):
    return str(len(name))

def home (request):
    tasks = Task.objects.all()
    tasks_titles = []
    for obj in tasks:
        tasks_titles.append(length_check(obj.title))
    display = ", ".join(tasks_titles)
    return HttpResponse(display)


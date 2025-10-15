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

def tasks_list(request):
    
    context = { "titles": list(Task.objects.all())}
    return render(request, 'todo_list/index1.html', context)

def ali_tasks(request):
    context = { "tasks": list(Task.objects.filter(belongsto=1)) }
    return render(request, 'todo_list/index3.html', context)
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

def students_tasks(request, st):
    context = { "tasks": list(Task.objects.filter(belongsto_id=st)) }
    return render(request, 'todo_list/index3.html', context)

"""یک view بنویسید که به دانشجو اجازه دهد وضعیت یک تسک خاص (done) را تغییر دهد (از انجام نشده به انجام شده و برعکس)  و در نهایت جزییات آن را نمایش دهد (با ارسال id هر تسک در url)"""
def mark_tasks(request, id):
    context = { "key" : Task.objects.filter(id=id)}
    return render(request, 'todo_list/index6.html', context)
    
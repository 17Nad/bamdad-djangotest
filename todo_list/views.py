from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *



def tasks_list(request):    
    context = { "titles": list(Task.objects.all())}
    return render(request, 'todo_list/index1.html', context)

def students_tasks(request, st):
    context = { "tasks": list(Task.objects.filter(belongsto_id=st)) }
    return render(request, 'todo_list/index3.html', context)

"""یک view بنویسید که به دانشجو اجازه دهد وضعیت یک تسک خاص (done) را تغییر دهد (از انجام نشده به انجام شده و برعکس)  و در نهایت جزییات آن را نمایش دهد (با ارسال id هر تسک در url)"""
def tasks_info(request, id): #TODO: use update method
    if request.method == "GET":
        context = { "key" : Task.objects.get(id=id),
                   "form" : TaskInfo } 
        return render(request, 'todo_list/index6.html', context)
    
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
 
def all_students(request):
    context = {"all": Student.objects.all()}
    return render(request, 'students/index.html', context)


"""یک view بنویسید که تمام دانشجویان با نمره بالاتر از عددی که در url وارد شده را از مدل Student دریافت کرده و در یک قالب HTML نمایش دهد(در تعریف url یک عبارت ورودی از نوع int داشته باشید- ارسال score در url)"""
def top_students(request, min_grade):
    context = {"top": list(Student.objects.filter(grade__gte=min_grade))}
    return render(request, 'students/index.html', context)

def new_student(request):
    Student.objects.create("new", "ea", 0)
    new = all_students(request)
    return new #??????????????????????

# def students_tasks(request):
#     context = {"tasks": Student.objects.filter(id=1)}
#     return render(request, 'students/index3.html', context)

def all_courses(request):
    context = { "all" : Course.objects.all()}
    return render(request, 'students/index4.html', context)

"""یک view بنویسید که جزییات یک course خاص (مانند عنوان، کد و دانشجویان ثبتنام شده) را نمایش دهد (بر اساس id هر course در url)"""
def select_courses(request, id):
    context = { "all" : Course.objects.filter(id=id)}
    return render(request, 'students/index4.html', context)


"""یک view بنویسید که تمام دوره های ثبت نام شده یک دانشجو را نمایش دهد (بر اساس id هر دانشجو در url)"""
def student_courses(request , id):
    context = {"key" : Student.objects.filter(id=id)}
    return render (request, 'students/index5.html', context)

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
        # return redirect ("students:studentDashboard")
        return render(request, studentFormPage, context)

def student_dashboard(request):
    return HttpResponse("this is your dashboard")

def new_course(request):
    courseFormPage = "students/index8.html"
    if request.method == "GET":
        return render(request, courseFormPage, {"form": CourseForm})
    elif request.method == "POST":
        try:            
            new = Course.objects.create(
                title=request.POST["title"],
                description=request.POST["description"],
                start=request.POST["start"],
                end=request.POST["end"] )
            context = {
                "form": CourseForm,
                "message0": """Course created successfully!\n
                          If you want to create another course, please fill the form."""}
        except ValueError:
            context = {
                "form": CourseForm,
                "message1": "Invalid date format. Please enter dates in this format: YYYY-MM-DD" }
        return render(request, courseFormPage, context)

from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import *

"""یک view بنویسید که فرم ساده ای برای ایجاد یک دانشجوی جدید (Student) باشد 
- اطلاعات وارد شده را در دیتابیس ذخیره کند
- حتما چک کند که username یکتا باشد و در غیر این صورت اجاز ثبت ندهد"""
# فرم student رو سر کلاس نوشته بودم اینبار user رو نوشتم
class UserRegister(View):
    template = 'authentication/register.html'
    def get(self, request):
        context = { "form": UserRegisterForm() }
        return render(request, self.template, context)
    
    def post(self, request):
        form = UserRegisterForm(request.POST)
        context = {
            'form': form,
            'message': 'Username or password is invalid.' }
        if form.is_valid():
            new = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password'] )
            if new:
                # return redirect('login')
                return HttpResponse("User registered successfully.")
        else:
            return render (request, self.template, context)
        
 # TODO: compelete ts       
class UserLogin(View):
    form = UserRegisterForm
    template = 'authentication/login.html'

    def get(self, request):
        return render (request, self.template, {"form": self.form})
    
    def post (self, request):
        info = AuthenticationForm(request, data=request.POST)
        if info.is_valid():
            user = info.get_user()
            if user and user.is_authenticated:
                login(request, user)
                return redirect ("students:studentDashboard")
        else: 
            context ={"form": self.form,
                      "message": "Username or password is invalid."}
            return render(request, self.template, context)
                   
    
class UserLogOut(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect("authentication:login")
        else: 
            return redirect("students:studentDashboard")

class UserDelete(View): #TODO: doesn't work yet
    def get(self, request):
        if request.user.is_authenticated:
            try:
                logout(request)
                request.user.delete()
                return redirect("authentication:register")
            except:
                return HttpResponse("<h1>Error</h1>")
        else:
            return HttpResponseForbidden("<h1>403: Access Denied</h1><p>You don't have permission to delete this user!</p>")

# object.is_valid()
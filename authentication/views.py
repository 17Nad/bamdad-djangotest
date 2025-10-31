from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
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
class LoginView(View):
    def get(self, request):
        pass
    
class LogOutView(View):
    def get(self, request):
        if request.user.is_authentucated:
            logout(request)
            return redirect("account:user-login")

class DeleteUser(View):
    def get(self, request):
        if request.user.is_authenticated:
            try:
                user = User.objects.get(id=user.request.id)
                user.delete()
                return redirect("authentication:register")
            except:
                return render()

# object.is_valid()
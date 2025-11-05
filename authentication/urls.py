from django.urls import path
from authentication.views import *

app_name = "authentication"
urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
    path("login/", UserLogin.as_view(), name="login"),
    path ("logout/", UserLogOut.as_view(), name="logout"),
    path ("delete-user/", UserDelete.as_view(), name="deleteUser")
]
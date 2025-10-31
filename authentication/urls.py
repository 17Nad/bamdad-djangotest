from django.urls import path
from authentication.views import *

urlpatterns = [
    path("register/", UserRegister.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
]
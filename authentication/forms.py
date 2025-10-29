from django.forms import ModelForm
from django.contrib.auth.models import User
from authentication.models import *

class UserRegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
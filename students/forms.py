from django.forms import ModelForm
from students.models import *

class StudentForm (ModelForm):
    class Meta:
        model = Student
        fields = ["major"]

class TeacherForm (ModelForm):
    class Meta:
        model = Teacher
        fields = ["major"]

class InitProfileForm (ModelForm):
    class Meta:
        model = Profile
        exclude= ["belongsto"]

class CourseForm (ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "start", "end", "is_active"]
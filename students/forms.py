from django.forms import ModelForm
from students.models import *

class StudentForm (ModelForm):
    class Meta:
        model = Student
        fields = ["name", "field"]

class CourseForm (ModelForm):
    class Meta:
        model = Course
        fields = ["title", "description", "start", "end"]
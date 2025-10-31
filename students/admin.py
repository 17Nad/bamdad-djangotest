from django.contrib import admin
from students.models import *

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Profile)
admin.site.register(Course)
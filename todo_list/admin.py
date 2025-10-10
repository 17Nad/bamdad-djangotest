from django.contrib import admin
from todo_list.models import *

admin.site.register(Task)
admin.site.register(Tag)
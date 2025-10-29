from django.forms import ModelForm
from todo_list.models import Task

class TaskInfo (ModelForm):
    class Meta:
        model = Task
        fields = exclude = ['belongsto']
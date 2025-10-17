from django.db import models
from students.models import Student



class Task(models.Model):
    title = models.CharField(max_length = 256)
    category = models.CharField(max_length= 64)
    description = models.TextField()
    deadline = models.DateTimeField()
    isdone = models.BooleanField(default = False)
    belongsto = models.ForeignKey(Student , on_delete = models.CASCADE, related_name="tasks")
    
    def __str__(self):
        return self.title
    
    
class Tag(models.Model):
    title = models.CharField(max_length=32)
    tasks = models.ManyToManyField(Task)
    
    def __str__(self):
        return self.title
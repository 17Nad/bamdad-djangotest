from django.db import models
# from todo_list.models import Task


class Student (models.Model):
    name = models.CharField(max_length=128)
    field = models.CharField(max_length=256)
    grade = models.PositiveIntegerField()
#    tasks = models.ForeignKey(Task)
    phone_number = models.CharField (max_length=13, default="+989000000000")

    def __str__(self):
        return self.name
    
    
class Course(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.title

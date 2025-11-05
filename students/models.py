from django.db import models
from django.contrib.auth.models import User
# from todo_list.models import Task



class Student (models.Model):
    name = models.CharField(max_length=128)
    field = models.CharField(max_length=256)
    grade = models.PositiveIntegerField(default=0)
#    tasks = models.ForeignKey(Task)
    user= models.OneToOneField("Profile", on_delete = models.CASCADE, related_name="student", null = True)
    def __str__(self):
        return self.name
    

class Teacher (models.Model):
    name = models.CharField(max_length=128)
    score = models.PositiveIntegerField(default=0)
    user= models.OneToOneField("Profile", on_delete = models.CASCADE, related_name="teacher" , null = True)
    def __str__(self):
        return self.name
    

# activity_status = {
#     0 : "offline",
#     1 : "online",
#     2 : "invisible",
#     3 : "do not disturb"
#}
# role = { 1 : Student, 2 : Teacher }

class Profile(models.Model):
    bio = models.TextField(max_length=512, default="")
    phone_number = models.CharField (max_length=13, default="+989000000000")
    birthday = models.DateField()
    #avatar = models.ImageField(null=True, blank=True)
    belongsto = models.OneToOneField(User, on_delete=models.CASCADE)
    # status = models.PositiveIntegerField(choices=activity_status)
    
    def __str__(self):
        return f"{self.belongsto.name}'s Profile"
    
    
class Course(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    students = models.ManyToManyField(Student, related_name="courses")
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL ,null=True, blank=True)

    def __str__(self):
        return self.title

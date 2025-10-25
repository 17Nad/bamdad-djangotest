from django.db import models
# from todo_list.models import Task



class Student (models.Model):
    name = models.CharField(max_length=128)
    field = models.CharField(max_length=256)
    grade = models.PositiveIntegerField(default=0)
#    tasks = models.ForeignKey(Task)
    phone_number = models.CharField (max_length=13, default="+989000000000")

    def __str__(self):
        return self.name
    
    
activity_status = {
    0 : "offline",
    1 : "online",
    2 : "invisible",
    3 : "do not disturb"
}
class Profile(models.Model):
    bio = models.TextField(max_length=512, default="")
    username = models.CharField(max_length=32)
    birthday = models.DateField()
    # avatar = models.ImageField()
    belongsto = models.OneToOneField(Student, on_delete=models.CASCADE, primary_key=True)
    status = models.PositiveIntegerField(choices=activity_status)

    def __str__(self):
        return self.belongsto.name + "'s Profile"
    
    
class Course(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return self.title

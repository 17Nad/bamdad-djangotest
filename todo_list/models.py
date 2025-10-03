from django.db import models

class Task(models.Model):
    title = models.CharField(max_length = 256)
    category = models.CharField(max_length= 64)
    description = models.TextField()
    deadline = models.DateTimeField()
    isdone = models.BooleanField(default = False)
    # user = models.ForeignKey(User)
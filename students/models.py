from django.db import models

class Student (models.Model):
    name = models.CharField(max_length=128)
    field = models.CharField(max_length=256)
    grade = models.IntegerField()
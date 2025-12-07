from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *


@receiver(post_save, sender = Profile) 
def determine_role(sender, instance, created, **kwargs):
    if created: #TODO: How do I trigger a signal with something being modified? (this should run when two conditions are true: when a profile is created and when is_teacher is determined(is_teacher can only be modified once))
        if instance.is_teacher:
            Teacher.objects.create(user = instance)
        else:
            Student.objects.create(user = instance)
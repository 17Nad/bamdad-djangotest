from django.db.models.signals import post_save, pre_save, post_delete, pre_delete
from django.dispatch import receiver
from .models import *

# TODO: not compeleted yet
@receiver(pre_save, sender = Student)
def create_profile(sender, instance, create, **keywargs):
    if create:
        Profile.objects.create (
            belongsto = instance.name,
            student = instance )

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from students.models import Profile

# TODO: not compeleted yet
@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create (
            belongsto = instance,
            name = first_name + ' ' + last_name )
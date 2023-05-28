from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender = User) 
# when a user is saved, send 'post_save' signal which going to be recived by reciver. this reciver is a 'create_profile' function which take four arguments.
def create_profile(sender, instance, created, **kwargs):
    #if created the create a profile using instance.
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
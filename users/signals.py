from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Profile, Location
from django.db.models.signals import pre_delete

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile_loc =  Location.objects.create()
        instance.location = profile_loc
        instance.save()

@receiver(pre_delete, sender=User)
def delete_profile(sender, instance, **kwargs):
    try:
        user_profile = Profile.objects.get(user=instance)
        if user_profile.photo:
            user_profile.photo.delete()
        user_profile.delete()
    except Profile.DoesNotExist:
        pass

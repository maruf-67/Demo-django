from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField, USZipCodeField
from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = USStateField(default='CA')
    zip_code = USZipCodeField(blank=True)

    def __str__(self):
        return f'Location {self.id}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path,null=True)
    bio = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
   
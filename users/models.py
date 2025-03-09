from django.db import models
from django.contrib.auth.models import User
import datetime

def upload_to(instance, filename):
    now = datetime.datetime.now()
    return 'images/{}/{}/{}'.format(now.year, now.month, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_to,null=True)
    bio = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    
   
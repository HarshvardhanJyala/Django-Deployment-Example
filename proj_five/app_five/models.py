from django.db import models
#this User (class) here is Django's build in, that y u will not see it specificaly mentioned here.
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)

    # addtionaol classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

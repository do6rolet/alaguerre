from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False)
    avatar = models.ImageField(upload_to='uploads/', blank=True, null=True) # need to install Pillow


User.userprofile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
# try to get userprofilel, if it is not exist, create it

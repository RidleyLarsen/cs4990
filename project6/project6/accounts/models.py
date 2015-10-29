from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=128)
    location = models.CharField(max_length=64, null=True, blank=True)
    following = models.ManyToManyField('Profile', blank=True)
    picture = models.ImageField(upload_to="profiles/%Y/%m/%d/", null=True, blank=True)

    def __unicode__(self):
        return self.user.username

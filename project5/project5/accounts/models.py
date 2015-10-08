from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User)
    address_1 = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)

    def __unicode__(self):
        return self.user.username

'''
passenger info:
    name
    address
    phone
    payment object
    account

Account:
    User FK (contrib.auth user)
    Address
    Phone
'''

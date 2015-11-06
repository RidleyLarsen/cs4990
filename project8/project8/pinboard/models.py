from django.db import models
from project8.accounts.models import Profile


class Pin(models.Model):
    profile = models.ForeignKey(Profile)
    link = models.URLField()
    title = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)


class Board(models.Model):
    profile = models.ForeignKey(Profile)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=200, blank=True, null=True)
    pins = models.ManyToManyField(Pin, blank=True)

import signals

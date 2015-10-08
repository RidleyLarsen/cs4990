from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('Approved', 'Approved'),
    ('Denied', 'Denied'),
    ('In Review', 'In Review'),
    ('New', 'New'),
)


class Suggestion(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default="New")
    categories = models.ManyToManyField('Category')

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Comment(models.Model):
    suggestion = models.ForeignKey(Suggestion)
    user = models.ForeignKey(User)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

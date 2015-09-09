from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField()

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(User)
    text = models.TextField()
    pub_date = models.DateTimeField()
    active = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category)

    @property
    def published(self):
        return self.pub_date < timezone.now()

    def __unicode__(self):
        return self.title

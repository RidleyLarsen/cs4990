from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField()
    parent_category = models.ForeignKey('Category', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Categories"

    @property
    def parent_categories(self):
        parent = self.parent_category
        acc = []
        while parent is not None:
            acc.append(parent)
            parent = parent.parent_category
        acc.reverse()
        return acc

    def __unicode__(self):
        str = "%s" % self.name
        parent = self.parent_category
        while parent is not None:
            str = "%s > %s" % (parent.name, str)
            parent = parent.parent_category
        return str


class Item(models.Model):
    name = models.CharField(max_length=24)
    description = models.TextField()
    categories = models.ManyToManyField('Category')
    quantity = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.name

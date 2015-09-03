from django.db import models

# Create your models here.
class PortfolioEntry(models.Model):
    name = models.CharField(max_length=64)
    photo = models.ImageField(upload_to="uploads/%Y/%m/%d")
    link = models.URLField(null=True, blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.name

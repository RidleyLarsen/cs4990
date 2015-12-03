from django.db import models
from django.contrib.auth.models import User


class Stage(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(help_text="The order this is displayed on the screen")
    description = models.TextField(blank=True, null=True)
    value = models.IntegerField(help_text="On a scale of 0 to 100 of the stage of the pipeline")


class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(max_length=200, blank=True, null=True)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)


class Contact(models.Model):
    company = models.ForeignKey(Company, blank=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200, blank=True, null=True)
    address2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    zipcode = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)


class Opportunity(models.Model):
    stage = models.ForeignKey(Stage)
    company = models.ForeignKey(Company, blank=True, null=True)
    contact = models.ForeignKey(Contact)
    value = models.FloatField(help_text="How much this opportunity is worth to the organization")
    source = models.ForeignKey(Campaign, help_text="How did this contact find out about us?")
    user = models.ForeignKey(User)
    create_date = models.DateTimeField(auto_now_add=True)


class Reminder(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateField()
    note = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)


class Report(models.Model):
    name = models.CharField(max_length=200)
    link = models.URLField()


class CallLog(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    date = models.DateTimeField(auto_now_add=True)
    note = models.TextField()
    user = models.ForeignKey(User)


class OpportunityStage(models.Model):
    opportunity = models.ForeignKey(Opportunity)
    stage = models.ForeignKey(Stage)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

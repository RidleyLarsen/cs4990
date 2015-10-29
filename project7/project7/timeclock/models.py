from dateutil import relativedelta
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.utils import timezone

# Create your models here.


class Volunteer(models.Model):
    user = models.OneToOneField(User, blank=True, null=True)
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=128)
    address_2 = models.CharField(max_length=128, blank=True, null=True)
    active = models.BooleanField(default=False, blank=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    emergency_contact = models.CharField(max_length=128, blank=True, null=True)
    emergency_contact_phone = models.CharField(max_length=24, blank=True, null=True)
    emergency_contact_relationship = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        verbose_name = 'Volunteer'
        verbose_name_plural = 'Volunteers'

    def active_recently(self):
        evts = Event.objects.filter(user=self.user)
        past = timezone.now()
        past = past - relativedelta(days=30)
        evts = evts.filter(time_in__gte=past)
        return evts.count() > 0
    active_recently.boolean = True

    def total_hours_tuple(self):
        hours = 0
        minutes = 0
        seconds = 0
        for obj in Event.objects.filter(user=self.user):
            duration = obj.duration_tuple()
            hours += duration[0]
            minutes += duration[1]
            seconds += duration[2]
            while seconds > 60:
                seconds -= 60
                minutes += 1
            while minutes >= 60:
                minutes -= 60
                hours += 1
        return (hours, minutes, seconds)

    @property
    def total_hours(self):
        return '%s hours, %s minutes, %s seconds' % self.total_hours_tuple()

    @property
    def total_hours_decimal(self):
        (hours, minutes, seconds) = self.total_hours_tuple()
        return hours + (minutes / 60.0) + (seconds / 3600.0)

    def __unicode__(self):
        return self.name + ' applied on ' + str(self.date)

    def get_absolute_url(self):
        return reverse('volunteer_detail', kwargs={'pk': self.pk})


class Event(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    time_in = models.DateTimeField()
    time_out = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    @property
    def volunteer(self):
        try:
            return Volunteer.objects.get(user=self.user)
        except:
            return None

    @property
    def duration(self):
        return '%d hours, %d minutes, %d seconds' % self.duration_tuple()

    def duration_tuple(self):
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
        if self.time_out and self.time_in:
            duration = self.time_out - self.time_in
        else:
            if self.time_in:
                duration = timezone.now() - self.time_in
            else:
                return (0, 0, 0)
        days += duration.days
        hours += days * 24 + duration.seconds // 3600
        minutes += (duration.seconds % 3600) // 60
        seconds += duration.seconds % 60
        while seconds > 60:
            seconds -= 60
            minutes += 1
        while minutes >= 60:
            minutes -= 60
            hours += 1
        return (hours, minutes, seconds)

    def __unicode__(self):
        return "" + self.user.username + " clocked in at " + unicode(self.time_in)

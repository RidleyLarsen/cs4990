# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_in', models.DateTimeField()),
                ('time_out', models.DateTimeField(null=True, blank=True)),
                ('notes', models.TextField(null=True, blank=True)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('photo', models.ImageField(null=True, upload_to=b'photos/%Y/%m/%d', blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=128, null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
                ('city', models.CharField(max_length=64, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('zip_code', models.CharField(max_length=10, null=True, blank=True)),
                ('phone', models.CharField(max_length=24, null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('emergency_contact', models.CharField(max_length=128, null=True, blank=True)),
                ('emergency_contact_phone', models.CharField(max_length=24, null=True, blank=True)),
                ('emergency_contact_relationship', models.CharField(max_length=24, null=True, blank=True)),
                ('work_experience', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Volunteer',
                'verbose_name_plural': 'Volunteers',
            },
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_profile_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.URLField()),
                ('title', models.CharField(max_length=128, null=True, blank=True)),
                ('description', models.CharField(max_length=200, null=True, blank=True)),
                ('picture', models.ImageField(null=True, upload_to=b'pins/%Y/%m/%d', blank=True)),
                ('profile', models.ForeignKey(to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='pins',
            field=models.ManyToManyField(to='pinboard.Pin', blank=True),
        ),
        migrations.AddField(
            model_name='board',
            name='profile',
            field=models.ForeignKey(to='accounts.Profile'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20150112_1840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
    ]

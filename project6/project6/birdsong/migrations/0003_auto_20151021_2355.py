# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20151021_2355'),
        ('birdsong', '0002_auto_20151015_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='mention',
            field=models.ForeignKey(related_name='mention', blank=True, to='accounts.Profile', null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='birdsong.Tag', blank=True),
        ),
    ]

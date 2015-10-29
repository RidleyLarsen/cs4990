# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdsong', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='reply_to',
            field=models.ForeignKey(blank=True, to='birdsong.Note', null=True),
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='birdsong.Tag', null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20151015_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address_1',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]

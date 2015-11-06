# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='zip_code',
            field=models.CharField(max_length=32),
            preserve_default=True,
        ),
    ]

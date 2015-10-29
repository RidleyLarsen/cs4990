# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birdsong', '0003_auto_20151021_2355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('timestamp',)},
        ),
    ]

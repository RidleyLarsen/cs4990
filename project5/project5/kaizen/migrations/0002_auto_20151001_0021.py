# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kaizen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suggestion',
            old_name='category',
            new_name='categories',
        ),
        migrations.AddField(
            model_name='comment',
            name='suggestion',
            field=models.ForeignKey(default=0, to='kaizen.Suggestion'),
            preserve_default=False,
        ),
    ]

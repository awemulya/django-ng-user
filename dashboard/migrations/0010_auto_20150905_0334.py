# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20150905_0331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='week',
        ),
        migrations.AddField(
            model_name='game',
            name='fixture',
            field=models.ForeignKey(related_name='fixture', default=1, to='dashboard.Fixture'),
            preserve_default=False,
        ),
    ]

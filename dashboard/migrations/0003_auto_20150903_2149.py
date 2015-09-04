# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150903_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='club',
            field=models.CharField(max_length=30, default='Manchester City'),
        ),
        migrations.AddField(
            model_name='players',
            name='position',
            field=models.CharField(max_length=12, default='foreward', choices=[('foreward', 'Foreward'), ('midfilder', 'Midfilder'), ('defender', 'Defender'), ('goalkeeper', 'GoalKeeper')]),
        ),
    ]

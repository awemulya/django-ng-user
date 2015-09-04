# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_remove_players_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='club',
            field=models.ForeignKey(to='dashboard.Club', null=True, related_name='players'),
        ),
    ]

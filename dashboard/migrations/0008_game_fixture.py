# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_players_club'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='fixture',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

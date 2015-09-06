# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_remove_game_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='player',
            field=models.ForeignKey(default=1, to='dashboard.Players', related_name='game'),
            preserve_default=False,
        ),
    ]

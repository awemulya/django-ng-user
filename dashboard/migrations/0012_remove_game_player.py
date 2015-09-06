# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_fixture_played'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='player',
        ),
    ]

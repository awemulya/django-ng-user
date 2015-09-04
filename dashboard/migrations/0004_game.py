# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20150903_2149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('week', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
                ('player', models.ForeignKey(to='dashboard.Players', related_name='game')),
            ],
        ),
    ]

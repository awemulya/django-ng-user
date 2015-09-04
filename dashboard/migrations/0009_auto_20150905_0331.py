# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_game_fixture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('week', models.IntegerField(default=0)),
                ('home_goals', models.IntegerField(default=0)),
                ('away_goals', models.IntegerField(default=0)),
                ('time', models.DateTimeField(null=True)),
                ('away', models.ForeignKey(to='dashboard.Club', related_name='away')),
                ('home', models.ForeignKey(to='dashboard.Club', related_name='home')),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='fixture',
        ),
    ]

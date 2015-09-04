# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(default='Manchester City', max_length=30)),
                ('established', models.DateField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='players',
            name='position',
            field=models.CharField(default='forward', choices=[('forward', 'Forward'), ('midfielder', 'Midfielder'), ('defender', 'Defender'), ('goalkeeper', 'GoalKeeper')], max_length=12),
        ),
    ]

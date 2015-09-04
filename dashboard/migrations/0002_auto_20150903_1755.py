# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='name',
            field=models.CharField(db_index=True, verbose_name='name', max_length=255),
        ),
    ]

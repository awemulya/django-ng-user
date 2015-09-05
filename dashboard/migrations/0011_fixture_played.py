# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20150905_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='played',
            field=models.BooleanField(default=False),
        ),
    ]

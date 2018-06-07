# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0033_auto_20180602_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group',
        ),
    ]

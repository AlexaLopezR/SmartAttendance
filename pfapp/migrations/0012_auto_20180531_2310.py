# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0011_auto_20180531_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmember',
            name='foto1',
        ),
        migrations.RemoveField(
            model_name='groupmember',
            name='foto2',
        ),
    ]

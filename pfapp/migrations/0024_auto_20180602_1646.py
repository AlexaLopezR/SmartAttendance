# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0023_auto_20180602_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='nombreint',
            field=models.CharField(max_length=80),
        ),
    ]

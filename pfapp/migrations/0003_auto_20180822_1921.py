# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0002_auto_20180820_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='correoint',
            field=models.EmailField(max_length=100),
        ),
    ]

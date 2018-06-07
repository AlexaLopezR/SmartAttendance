# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0027_auto_20180602_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ForeignKey(default=None, to='pfapp.Users'),
        ),
    ]

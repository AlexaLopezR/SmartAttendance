# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0025_auto_20180602_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='owner',
            new_name='users',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0026_auto_20180602_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='users',
            new_name='user',
        ),
    ]

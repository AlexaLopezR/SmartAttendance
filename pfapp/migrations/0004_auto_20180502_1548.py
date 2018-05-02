# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0003_groups'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='groups',
            name='hora',
        ),
    ]

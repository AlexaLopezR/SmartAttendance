# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0032_group_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group',
            field=models.ForeignKey(default=1, to='pfapp.Users'),
        ),
    ]

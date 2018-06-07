# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0024_auto_20180602_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(to='pfapp.Users'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0020_auto_20180602_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(to='pfapp.Users', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0048_auto_20180612_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='cod1',
            field=models.CommaSeparatedIntegerField(max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0005_auto_20180528_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmembers',
            name='nombreGroup',
            field=models.CharField(default=datetime.datetime(2018, 5, 28, 17, 0, 7, 696232, tzinfo=utc), max_length=80),
            preserve_default=False,
        ),
    ]

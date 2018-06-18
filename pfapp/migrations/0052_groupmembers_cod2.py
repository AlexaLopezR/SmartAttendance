# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0051_auto_20180615_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmembers',
            name='cod2',
            field=models.TextField(null=True),
        ),
    ]

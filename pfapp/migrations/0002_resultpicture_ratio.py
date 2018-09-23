# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resultpicture',
            name='ratio',
            field=models.CharField(max_length=10, null=True),
        ),
    ]

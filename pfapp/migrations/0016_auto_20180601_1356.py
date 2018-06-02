# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0015_auto_20180601_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='foto1',
            field=models.ImageField(upload_to=b'pfapp/images/'),
        ),
    ]

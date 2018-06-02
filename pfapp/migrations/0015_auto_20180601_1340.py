# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0014_auto_20180531_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='foto1',
            field=models.FileField(upload_to=b'images/'),
        ),
    ]

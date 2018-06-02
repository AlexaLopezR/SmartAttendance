# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0016_auto_20180601_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmembers',
            name='foto2',
            field=models.ImageField(default=b'default.jpg', upload_to=b'pfapp/images/'),
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='foto1',
            field=models.ImageField(default=b'default.jpg', upload_to=b'pfapp/images/'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0012_auto_20180531_2310'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmember',
            name='foto1',
            field=models.ImageField(default=b'default.jpg', upload_to=b'pfapp/images/'),
        ),
    ]

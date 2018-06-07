# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0038_auto_20180607_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ForeignKey(db_column=b'username', default=1, to=settings.AUTH_USER_MODEL),
        ),
    ]

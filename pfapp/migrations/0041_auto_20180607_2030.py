# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0040_auto_20180607_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='user',
            field=models.ForeignKey(db_column=b'user_id', default=2, to=settings.AUTH_USER_MODEL),
        ),
    ]

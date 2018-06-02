# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0017_auto_20180601_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymember',
            name='profile',
        ),
        migrations.DeleteModel(
            name='FamilyMember',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]

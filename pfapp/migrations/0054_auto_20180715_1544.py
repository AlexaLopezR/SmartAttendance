# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0053_auto_20180619_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='grupo',
            new_name='group',
        ),
        migrations.RenameField(
            model_name='groupmembers',
            old_name='group',
            new_name='groupid',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0006_groupmembers_nombregroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmembers',
            name='nombreGroup',
        ),
        migrations.AddField(
            model_name='groups',
            name='integrantess',
            field=models.ManyToManyField(to='pfapp.GroupMembers'),
        ),
    ]

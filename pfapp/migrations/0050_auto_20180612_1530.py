# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0049_auto_20180612_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='cod1',
            field=models.BinaryField(),
        ),
    ]

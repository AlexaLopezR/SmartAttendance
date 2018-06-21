# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0052_groupmembers_cod2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadphoto',
            old_name='fotogrupo',
            new_name='picture',
        ),
    ]

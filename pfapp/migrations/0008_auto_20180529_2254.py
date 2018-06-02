# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0007_auto_20180529_2130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groups',
            old_name='nombreGrupo',
            new_name='grupo',
        ),
        migrations.RenameField(
            model_name='groups',
            old_name='integrantess',
            new_name='integrantes',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0004_auto_20180502_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreint', models.CharField(max_length=80)),
                ('correoint', models.EmailField(unique=True, max_length=100)),
                ('foto1', models.ImageField(upload_to=b'pfapp/images/')),
                ('foto2', models.ImageField(upload_to=b'pfapp/images/')),
            ],
        ),
        migrations.RenameField(
            model_name='groups',
            old_name='nombregrupo',
            new_name='nombreGrupo',
        ),
    ]

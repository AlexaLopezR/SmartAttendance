# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombrecompleto', models.CharField(max_length=80)),
                ('correo', models.EmailField(unique=True, max_length=100)),
                ('contrasena', models.CharField(max_length=32)),
            ],
        ),
    ]

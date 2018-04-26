# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0002_auto_20180424_1353'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombregrupo', models.CharField(max_length=80)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('hora', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

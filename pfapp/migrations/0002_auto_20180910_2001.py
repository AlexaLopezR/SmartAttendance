# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='picture2',
            field=models.ImageField(null=True, upload_to=b'pfapp/images/'),
        ),
    ]

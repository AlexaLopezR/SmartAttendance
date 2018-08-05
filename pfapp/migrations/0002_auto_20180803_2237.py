# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pfapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadphoto',
            name='idgroup',
            field=models.ForeignKey(default=1, to='pfapp.Group'),
        ),
        migrations.AddField(
            model_name='uploadphoto',
            name='result',
            field=models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path),
        ),
    ]

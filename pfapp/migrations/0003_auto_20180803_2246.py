# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pfapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0002_auto_20180803_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result', models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path)),
            ],
        ),
        migrations.RemoveField(
            model_name='uploadphoto',
            name='result',
        ),
    ]

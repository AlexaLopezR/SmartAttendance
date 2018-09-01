# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pfapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resultpicture',
            old_name='result',
            new_name='result1',
        ),
        migrations.RenameField(
            model_name='uploadphoto',
            old_name='picture',
            new_name='picture1',
        ),
        migrations.AddField(
            model_name='resultpicture',
            name='result2',
            field=models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path),
        ),
        migrations.AddField(
            model_name='uploadphoto',
            name='picture2',
            field=models.ImageField(default=b'default.jpg', upload_to=b'pfapp/images/'),
        ),
    ]

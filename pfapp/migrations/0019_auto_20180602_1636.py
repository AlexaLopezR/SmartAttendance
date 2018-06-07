# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import pfapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0018_auto_20180602_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fotogrupo', models.ImageField(default=b'default.jpg', upload_to=b'pfapp/images/')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='owner',
            field=models.ForeignKey(to='pfapp.Users', null=True),
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='foto1',
            field=models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='foto2',
            field=models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path),
        ),
        migrations.AlterField(
            model_name='groupmembers',
            name='nombreint',
            field=models.CharField(default=0, max_length=80),
        ),
    ]

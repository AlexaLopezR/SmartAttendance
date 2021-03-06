# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import pfapp.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=80)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMembers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreint', models.CharField(max_length=80)),
                ('correoint', models.EmailField(max_length=100)),
                ('foto1', models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path)),
                ('foto2', models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path)),
                ('cod1', models.TextField()),
                ('cod2', models.TextField(null=True)),
                ('groupid', models.ForeignKey(to='pfapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='ResultPicture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('result1', models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path)),
                ('result2', models.ImageField(default=b'default.jpg', upload_to=pfapp.models.get_image_path)),
                ('assisted', models.CharField(max_length=1000)),
                ('missing', models.CharField(max_length=1000)),
                ('fecha', models.CharField(max_length=1000)),
                ('idassisted', models.CharField(max_length=1000)),
                ('idgroup', models.ForeignKey(default=1, to='pfapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='UploadPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture1', models.ImageField(default=b'default.jpg', upload_to=b'pfapp/images/')),
                ('picture2', models.ImageField(null=True, upload_to=b'pfapp/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=80)),
                ('correo', models.EmailField(max_length=100)),
                ('contrasena', models.CharField(max_length=32)),
            ],
        ),
    ]

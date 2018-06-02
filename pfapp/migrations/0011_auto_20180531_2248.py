# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0010_auto_20180531_2046'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreint', models.CharField(max_length=80)),
                ('correoint', models.EmailField(unique=True, max_length=100)),
                ('foto1', models.ImageField(upload_to=b'pfapp/images/')),
                ('foto2', models.ImageField(upload_to=b'pfapp/images/')),
            ],
        ),
        migrations.RenameModel(
            old_name='Groups',
            new_name='Group',
        ),
        migrations.RemoveField(
            model_name='members',
            name='group',
        ),
        migrations.DeleteModel(
            name='Members',
        ),
        migrations.AddField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(to='pfapp.Group'),
        ),
    ]

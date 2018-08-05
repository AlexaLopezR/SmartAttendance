# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0003_auto_20180803_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadphoto',
            name='idgroup',
        ),
        migrations.AddField(
            model_name='resultpicture',
            name='idgroup',
            field=models.ForeignKey(default=1, to='pfapp.Group'),
        ),
    ]

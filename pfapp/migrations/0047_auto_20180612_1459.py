# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import re
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pfapp', '0046_auto_20180612_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmembers',
            name='cod1',
            field=models.CharField(default=b'', max_length=30, null=True, blank=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+\\Z'), 'Enter only digits separated by commas.', 'invalid')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0011_auto_20180401_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='confirm',
            field=models.CharField(null=True, blank=True, max_length=2),
        ),
    ]

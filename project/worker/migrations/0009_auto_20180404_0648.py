# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0008_auto_20180403_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ptype',
            field=models.TextField(max_length=250, blank=True, null=True),
        ),
    ]

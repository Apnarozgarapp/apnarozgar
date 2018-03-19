# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_auto_20180316_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.FloatField(null=True, blank=True),
        ),
    ]

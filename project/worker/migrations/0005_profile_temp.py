# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20180330_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='temp',
            field=models.CharField(blank=True, null=True, max_length=2),
        ),
    ]

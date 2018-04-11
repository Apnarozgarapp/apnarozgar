# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0017_auto_20180411_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contractor',
            field=models.PositiveSmallIntegerField(null=True, blank=True, default=0),
        ),
    ]

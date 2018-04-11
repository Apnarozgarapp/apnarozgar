# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0015_auto_20180411_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor',
            name='username',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

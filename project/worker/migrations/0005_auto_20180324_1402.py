# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20180317_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Twork',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='worker_age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

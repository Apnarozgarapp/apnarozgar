# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0016_auto_20180410_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='target',
            field=models.CharField(null=True, max_length=2, blank=True),
        ),
    ]

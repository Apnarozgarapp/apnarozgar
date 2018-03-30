# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20180329_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='temp',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
    ]

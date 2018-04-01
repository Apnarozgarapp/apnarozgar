# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0009_auto_20180401_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='temp1',
            field=models.CharField(null=True, blank=True, max_length=2),
        ),
    ]

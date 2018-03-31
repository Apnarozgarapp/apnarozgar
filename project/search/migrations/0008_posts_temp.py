# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20180330_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='temp',
            field=models.CharField(null=True, max_length=2, blank=True),
        ),
    ]

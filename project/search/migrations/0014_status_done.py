# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0013_auto_20180402_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='done',
            field=models.CharField(blank=True, null=True, max_length=2),
        ),
    ]

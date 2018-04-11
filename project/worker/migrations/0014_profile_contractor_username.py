# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0013_current_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='contractor_username',
            field=models.CharField(null=True, blank=True, max_length=50),
        ),
    ]

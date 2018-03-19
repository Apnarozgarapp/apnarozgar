# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='geocode',
            new_name='lat',
        ),
        migrations.AddField(
            model_name='location',
            name='lng',
            field=models.CharField(max_length=50, blank=True, null=True),
        ),
    ]

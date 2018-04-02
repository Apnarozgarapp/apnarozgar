# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_profile_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='nhirer',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

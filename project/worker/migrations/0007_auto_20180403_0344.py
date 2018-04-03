# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0006_profile_nhirer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description1',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description2',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description3',
            field=models.TextField(max_length=500, blank=True, null=True),
        ),
    ]

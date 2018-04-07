# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0014_status_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='Nworker',
            field=models.CharField(null=True, max_length=10, blank=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='distance',
            field=models.FloatField(null=True, blank=True),
        ),
    ]

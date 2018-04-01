# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0008_posts_temp'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='end_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='status',
            name='start_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

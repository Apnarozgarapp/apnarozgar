# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0010_posts_temp1'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='pay',
            field=models.CharField(blank=True, null=True, max_length=2),
        ),
        migrations.AddField(
            model_name='status',
            name='rating',
            field=models.CharField(blank=True, null=True, max_length=2),
        ),
    ]

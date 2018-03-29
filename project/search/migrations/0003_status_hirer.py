# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_posts_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='hirer',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]

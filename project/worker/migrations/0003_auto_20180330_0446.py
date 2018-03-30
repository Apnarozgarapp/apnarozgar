# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_profile_joinrequst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='joinrequst',
            field=models.CharField(null=True, blank=True, max_length=2),
        ),
    ]

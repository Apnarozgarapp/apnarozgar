# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0012_status_confirm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='pay',
        ),
        migrations.RemoveField(
            model_name='status',
            name='rating',
        ),
    ]

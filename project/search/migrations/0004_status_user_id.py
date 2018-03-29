# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_status_hirer'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

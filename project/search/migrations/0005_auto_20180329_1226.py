# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_status_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='hirer_status',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='status',
            name='worker_status',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]

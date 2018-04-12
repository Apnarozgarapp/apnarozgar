# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_remove_contractor_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='age',
            new_name='dis',
        ),
        migrations.AddField(
            model_name='contractor',
            name='dis',
            field=models.FloatField(null=True, blank=True),
        ),
    ]

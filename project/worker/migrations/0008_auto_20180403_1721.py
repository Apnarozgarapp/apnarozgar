# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0007_auto_20180403_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Twork',
            new_name='ptype',
        ),
        migrations.AddField(
            model_name='profile',
            name='description11',
            field=models.TextField(null=True, blank=True, max_length=500),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0016_auto_20180411_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractor',
            name='id',
        ),
        migrations.AddField(
            model_name='contractor',
            name='cid',
            field=models.AutoField(serialize=False, primary_key=True, default=1),
            preserve_default=False,
        ),
    ]

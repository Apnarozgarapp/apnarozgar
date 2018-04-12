# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0005_auto_20180412_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor',
            name='joinrequest',
            field=models.CharField(max_length=2, null=True, blank=True),
        ),
    ]

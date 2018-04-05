# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180404_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='done',
            field=models.CharField(null=True, blank=True, max_length=2),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_feedback_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='target',
            field=models.CharField(max_length=2, blank=True, null=True),
        ),
    ]

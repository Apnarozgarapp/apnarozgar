# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20180324_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts_of_work',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

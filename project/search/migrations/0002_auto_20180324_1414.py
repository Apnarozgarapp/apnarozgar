# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts_of_work',
            name='Twork',
            field=models.CharField(null=True, blank=True, max_length=250),
        ),
    ]

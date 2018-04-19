# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginAs',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='pmode',
            field=models.CharField(null=True, max_length=50, blank=True),
        ),
    ]

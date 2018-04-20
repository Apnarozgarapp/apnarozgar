# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20180419_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAs',
            fields=[
                ('username', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('loginas', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('geocode', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
    ]

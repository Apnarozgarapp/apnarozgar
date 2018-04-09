# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0012_auto_20180406_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='Current_location',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('address', models.CharField(null=True, max_length=250, blank=True)),
                ('lat', models.CharField(null=True, max_length=50, blank=True)),
                ('lng', models.CharField(null=True, max_length=50, blank=True)),
                ('time', models.CharField(null=True, max_length=50, blank=True)),
            ],
        ),
    ]

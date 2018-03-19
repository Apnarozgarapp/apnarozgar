# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginAs',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('loginas', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_otp',
            fields=[
                ('username', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=5)),
            ],
        ),
    ]

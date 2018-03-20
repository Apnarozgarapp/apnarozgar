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
                ('username', models.CharField(primary_key=True, serialize=False, max_length=100)),
                ('loginas', models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_otp',
            fields=[
                ('username', models.CharField(primary_key=True, serialize=False, max_length=100)),
                ('aadhar', models.CharField(max_length=12)),
                ('otp', models.CharField(max_length=5)),
            ],
        ),
    ]

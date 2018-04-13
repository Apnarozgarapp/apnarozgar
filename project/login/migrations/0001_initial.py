# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(serialize=False, primary_key=True)),
                ('userhirer', models.CharField(blank=True, null=True, max_length=100)),
                ('userworker', models.CharField(blank=True, null=True, max_length=100)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('feedback1', models.TextField(blank=True, null=True, max_length=100)),
                ('feedback2', models.TextField(blank=True, null=True, max_length=100)),
                ('feedback3', models.TextField(blank=True, null=True, max_length=100)),
                ('description', models.TextField(blank=True, null=True, max_length=200)),
                ('pmode', models.CharField(blank=True, null=True, max_length=2)),
                ('pdate', models.DateField(blank=True, null=True)),
                ('done', models.CharField(blank=True, null=True, max_length=2)),
                ('target', models.CharField(blank=True, null=True, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='LoginAs',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('loginas', models.CharField(null=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_otp',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('aadhar', models.CharField(max_length=12)),
                ('otp', models.CharField(max_length=5)),
            ],
        ),
    ]

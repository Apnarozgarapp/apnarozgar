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
                ('userhirer', models.CharField(blank=True, max_length=100, null=True)),
                ('userworker', models.CharField(blank=True, max_length=100, null=True)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('feedback1', models.TextField(blank=True, max_length=100, null=True)),
                ('feedback2', models.TextField(blank=True, max_length=100, null=True)),
                ('feedback3', models.TextField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('pmode', models.CharField(blank=True, max_length=2, null=True)),
                ('pdate', models.DateField(blank=True, null=True)),
                ('done', models.CharField(blank=True, max_length=2, null=True)),
                ('target', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoginAs',
            fields=[
                ('username', models.CharField(serialize=False, max_length=100, primary_key=True)),
                ('loginas', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration_otp',
            fields=[
                ('username', models.CharField(serialize=False, max_length=100, primary_key=True)),
                ('aadhar', models.CharField(max_length=12)),
                ('otp', models.CharField(max_length=5)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(blank=True, null=True, max_length=100)),
                ('s_contact', models.CharField(blank=True, null=True, max_length=50)),
                ('rskill', models.CharField(blank=True, null=True, max_length=100)),
                ('street', models.CharField(blank=True, null=True, max_length=250)),
                ('location', models.CharField(blank=True, null=True, max_length=250)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('Nworker', models.CharField(blank=True, null=True, max_length=10)),
                ('Twork', models.CharField(blank=True, null=True, max_length=250)),
                ('description', models.TextField(blank=True, null=True, max_length=500)),
                ('lat', models.CharField(blank=True, null=True, max_length=50)),
                ('lng', models.CharField(blank=True, null=True, max_length=50)),
                ('status', models.CharField(blank=True, null=True, max_length=50)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('temp', models.CharField(blank=True, null=True, max_length=2)),
                ('target', models.CharField(blank=True, null=True, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(serialize=False, primary_key=True)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('hirer', models.CharField(blank=True, null=True, max_length=100)),
                ('worker', models.CharField(blank=True, null=True, max_length=100)),
                ('userhirer', models.CharField(blank=True, null=True, max_length=100)),
                ('userworker', models.CharField(blank=True, null=True, max_length=100)),
                ('hirer_status', models.IntegerField(blank=True, null=True)),
                ('worker_status', models.IntegerField(blank=True, null=True)),
                ('confirm', models.CharField(blank=True, null=True, max_length=2)),
                ('temp', models.CharField(blank=True, null=True, max_length=2)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('done', models.CharField(blank=True, null=True, max_length=2)),
                ('target', models.CharField(blank=True, null=True, max_length=2)),
            ],
        ),
    ]

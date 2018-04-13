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
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('rskill', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('Nworker', models.CharField(blank=True, max_length=10, null=True)),
                ('Twork', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('lat', models.CharField(blank=True, max_length=50, null=True)),
                ('lng', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
                ('distance', models.FloatField(blank=True, null=True)),
                ('temp', models.CharField(blank=True, max_length=2, null=True)),
                ('target', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(serialize=False, primary_key=True)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('hirer', models.CharField(blank=True, max_length=100, null=True)),
                ('worker', models.CharField(blank=True, max_length=100, null=True)),
                ('userhirer', models.CharField(blank=True, max_length=100, null=True)),
                ('userworker', models.CharField(blank=True, max_length=100, null=True)),
                ('hirer_status', models.IntegerField(blank=True, null=True)),
                ('worker_status', models.IntegerField(blank=True, null=True)),
                ('confirm', models.CharField(blank=True, max_length=2, null=True)),
                ('temp', models.CharField(blank=True, max_length=2, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('done', models.CharField(blank=True, max_length=2, null=True)),
                ('target', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]

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
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('s_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('rskill', models.CharField(max_length=100, null=True, blank=True)),
                ('street', models.CharField(max_length=250, null=True, blank=True)),
                ('location', models.CharField(max_length=250, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('Nworker', models.CharField(max_length=10, null=True, blank=True)),
                ('Twork', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('lat', models.CharField(max_length=50, null=True, blank=True)),
                ('lng', models.CharField(max_length=50, null=True, blank=True)),
                ('status', models.CharField(max_length=50, null=True, blank=True)),
                ('distance', models.FloatField(null=True, blank=True)),
                ('temp', models.CharField(max_length=2, null=True, blank=True)),
                ('target', models.CharField(max_length=2, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField(null=True, blank=True)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('hirer', models.CharField(max_length=100, null=True, blank=True)),
                ('worker', models.CharField(max_length=100, null=True, blank=True)),
                ('userhirer', models.CharField(max_length=100, null=True, blank=True)),
                ('userworker', models.CharField(max_length=100, null=True, blank=True)),
                ('hirer_status', models.IntegerField(null=True, blank=True)),
                ('worker_status', models.IntegerField(null=True, blank=True)),
                ('confirm', models.CharField(max_length=2, null=True, blank=True)),
                ('temp', models.CharField(max_length=2, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('done', models.CharField(max_length=2, null=True, blank=True)),
                ('target', models.CharField(max_length=2, null=True, blank=True)),
            ],
        ),
    ]

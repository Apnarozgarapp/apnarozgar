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
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('s_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('rskill', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('Nworker', models.IntegerField(blank=True, null=True)),
                ('Twork', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('lat', models.CharField(blank=True, max_length=50, null=True)),
                ('lng', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('status_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('worker', models.CharField(blank=True, max_length=100, null=True)),
                ('hirer_status', models.CharField(blank=True, max_length=10, null=True)),
                ('worker_status', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts_of_work',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('s_contact', models.CharField(null=True, blank=True, max_length=50)),
                ('rskill', models.CharField(null=True, blank=True, max_length=100)),
                ('street', models.CharField(null=True, blank=True, max_length=250)),
                ('location', models.CharField(null=True, blank=True, max_length=250)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('Nworker', models.IntegerField(null=True, blank=True)),
                ('Twork', models.CharField(null=True, blank=True, max_length=100)),
                ('description', models.TextField(null=True, blank=True, max_length=500)),
                ('lat', models.CharField(null=True, blank=True, max_length=50)),
                ('lng', models.CharField(null=True, blank=True, max_length=50)),
                ('status', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('postid', models.IntegerField(null=True, blank=True)),
                ('worker', models.CharField(null=True, blank=True, max_length=100)),
                ('hirer_status', models.CharField(null=True, blank=True, max_length=10)),
                ('worker_status', models.CharField(null=True, blank=True, max_length=10)),
            ],
        ),
    ]

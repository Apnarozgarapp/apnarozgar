# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0014_profile_contractor_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('username', models.CharField(null=True, blank=True, max_length=50)),
                ('skill', models.CharField(null=True, blank=True, max_length=100)),
                ('nofworker', models.IntegerField(null=True, blank=True)),
                ('nameof_worker', models.CharField(null=True, blank=True, max_length=1024)),
                ('equipment', models.CharField(null=True, blank=True, max_length=250)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('experience', models.CharField(null=True, blank=True, max_length=250)),
                ('description1', models.TextField(null=True, blank=True, max_length=250)),
                ('description2', models.TextField(null=True, blank=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contractor_username',
        ),
    ]

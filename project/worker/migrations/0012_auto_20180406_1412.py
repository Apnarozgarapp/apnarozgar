# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0011_auto_20180405_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='ptype',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='worker_age',
        ),
        migrations.AddField(
            model_name='profile',
            name='loginas',
            field=models.TextField(max_length=10, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description1',
            field=models.TextField(max_length=250, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description11',
            field=models.TextField(max_length=250, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description2',
            field=models.TextField(max_length=250, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description3',
            field=models.TextField(max_length=250, blank=True, null=True),
        ),
    ]

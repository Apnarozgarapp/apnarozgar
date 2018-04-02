# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('userhirer', models.CharField(blank=True, max_length=100, null=True)),
                ('userworker', models.CharField(blank=True, max_length=100, null=True)),
                ('post_id', models.IntegerField(blank=True, null=True)),
                ('feedback', models.TextField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=2, null=True)),
                ('pay', models.CharField(blank=True, max_length=2, null=True)),
            ],
        ),
    ]

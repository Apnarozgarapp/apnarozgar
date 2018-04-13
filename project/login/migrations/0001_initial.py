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
<<<<<<< HEAD
                ('userhirer', models.CharField(null=True, blank=True, max_length=100)),
                ('userworker', models.CharField(null=True, blank=True, max_length=100)),
                ('post_id', models.IntegerField(null=True, blank=True)),
                ('feedback1', models.TextField(null=True, blank=True, max_length=100)),
                ('feedback2', models.TextField(null=True, blank=True, max_length=100)),
                ('feedback3', models.TextField(null=True, blank=True, max_length=100)),
                ('description', models.TextField(null=True, blank=True, max_length=200)),
                ('pmode', models.CharField(null=True, blank=True, max_length=2)),
                ('pdate', models.DateField(null=True, blank=True)),
                ('done', models.CharField(null=True, blank=True, max_length=2)),
                ('target', models.CharField(null=True, blank=True, max_length=2)),
=======
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
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
            ],
        ),
        migrations.CreateModel(
            name='LoginAs',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(serialize=False, primary_key=True, max_length=100)),
                ('loginas', models.CharField(null=True, max_length=50)),
=======
                ('username', models.CharField(serialize=False, max_length=100, primary_key=True)),
                ('loginas', models.CharField(max_length=50, null=True)),
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
            ],
        ),
        migrations.CreateModel(
            name='Registration_otp',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(serialize=False, primary_key=True, max_length=100)),
=======
                ('username', models.CharField(serialize=False, max_length=100, primary_key=True)),
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
                ('aadhar', models.CharField(max_length=12)),
                ('otp', models.CharField(max_length=5)),
            ],
        ),
    ]

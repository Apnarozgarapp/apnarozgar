# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('lat', models.CharField(null=True, blank=True, max_length=50)),
                ('lng', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('s_contact', models.CharField(null=True, blank=True, max_length=50)),
                ('age', models.FloatField(null=True, blank=True)),
                ('street', models.CharField(null=True, blank=True, max_length=250)),
                ('address', models.CharField(null=True, blank=True, max_length=250)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('skill1', models.CharField(null=True, blank=True, max_length=100)),
                ('skill2', models.CharField(null=True, blank=True, max_length=100)),
                ('skill3', models.CharField(null=True, blank=True, max_length=100)),
                ('description', models.TextField(null=True, blank=True, max_length=500)),
                ('min_salary', models.IntegerField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('Twork', models.CharField(null=True, blank=True, max_length=250)),
                ('worker_age', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]

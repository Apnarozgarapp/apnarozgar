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
            name='Profile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('s_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('street', models.CharField(blank=True, max_length=250, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('skill1', models.CharField(blank=True, max_length=100, null=True)),
                ('skill2', models.CharField(blank=True, max_length=100, null=True)),
                ('skill3', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

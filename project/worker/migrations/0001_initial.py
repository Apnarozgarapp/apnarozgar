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
            name='Contractor',
            fields=[
                ('cid', models.AutoField(serialize=False, primary_key=True)),
                ('username', models.IntegerField(null=True, blank=True)),
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
        migrations.CreateModel(
            name='Current_location',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('address', models.CharField(null=True, blank=True, max_length=250)),
                ('lat', models.CharField(null=True, blank=True, max_length=50)),
                ('lng', models.CharField(null=True, blank=True, max_length=50)),
                ('time', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('username', models.CharField(serialize=False, primary_key=True, max_length=50)),
                ('lat', models.CharField(null=True, blank=True, max_length=50)),
                ('lng', models.CharField(null=True, blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL)),
                ('s_contact', models.CharField(null=True, blank=True, max_length=50)),
                ('age', models.FloatField(null=True, blank=True)),
                ('street', models.CharField(null=True, blank=True, max_length=250)),
                ('address', models.CharField(null=True, blank=True, max_length=250)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('skill1', models.CharField(null=True, blank=True, max_length=100)),
                ('skill2', models.CharField(null=True, blank=True, max_length=100)),
                ('skill3', models.CharField(null=True, blank=True, max_length=100)),
                ('description1', models.TextField(null=True, blank=True, max_length=250)),
                ('description2', models.TextField(null=True, blank=True, max_length=250)),
                ('description3', models.TextField(null=True, blank=True, max_length=250)),
                ('description', models.TextField(null=True, blank=True, max_length=500)),
                ('description11', models.TextField(null=True, blank=True, max_length=250)),
                ('min_salary', models.IntegerField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('nhirer', models.IntegerField(null=True, blank=True)),
                ('loginas', models.TextField(null=True, blank=True, max_length=10)),
                ('joinrequest', models.CharField(null=True, blank=True, max_length=2)),
                ('temp', models.CharField(null=True, blank=True, max_length=2)),
                ('ac', models.CharField(null=True, blank=True, max_length=100)),
                ('ifsc', models.CharField(null=True, blank=True, max_length=100)),
                ('paytm', models.CharField(null=True, blank=True, max_length=100)),
                ('upi', models.CharField(null=True, blank=True, max_length=100)),
                ('acname', models.CharField(null=True, blank=True, max_length=100)),
                ('bank', models.CharField(null=True, blank=True, max_length=100)),
                ('mode', models.CharField(null=True, blank=True, max_length=100)),
                ('contractor', models.PositiveSmallIntegerField(null=True, default=0, blank=True)),
            ],
        ),
    ]

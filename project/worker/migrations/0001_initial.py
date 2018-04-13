# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('cid', models.AutoField(serialize=False, primary_key=True)),
                ('skill', models.CharField(max_length=100, blank=True, null=True)),
                ('nofworker', models.IntegerField(blank=True, null=True)),
                ('nameof_worker', models.CharField(max_length=1024, blank=True, null=True)),
                ('equipment', models.CharField(max_length=250, blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('experience', models.CharField(max_length=250, blank=True, null=True)),
                ('description1', models.TextField(max_length=250, blank=True, null=True)),
                ('description2', models.TextField(max_length=100, blank=True, null=True)),
                ('dis', models.FloatField(blank=True, null=True)),
                ('joinrequest', models.CharField(max_length=2, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Current_location',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=250, blank=True, null=True)),
                ('lat', models.CharField(max_length=50, blank=True, null=True)),
                ('lng', models.CharField(max_length=50, blank=True, null=True)),
                ('time', models.CharField(max_length=50, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('lat', models.CharField(max_length=50, blank=True, null=True)),
                ('lng', models.CharField(max_length=50, blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, primary_key=True, serialize=False)),
                ('s_contact', models.CharField(max_length=50, blank=True, null=True)),
                ('dis', models.FloatField(blank=True, null=True)),
                ('street', models.CharField(max_length=250, blank=True, null=True)),
                ('address', models.CharField(max_length=250, blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('skill1', models.CharField(max_length=100, blank=True, null=True)),
                ('skill2', models.CharField(max_length=100, blank=True, null=True)),
                ('skill3', models.CharField(max_length=100, blank=True, null=True)),
                ('description1', models.TextField(max_length=250, blank=True, null=True)),
                ('description2', models.TextField(max_length=250, blank=True, null=True)),
                ('description3', models.TextField(max_length=250, blank=True, null=True)),
                ('description', models.TextField(max_length=500, blank=True, null=True)),
                ('description11', models.TextField(max_length=250, blank=True, null=True)),
                ('min_salary', models.IntegerField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('nhirer', models.IntegerField(blank=True, null=True)),
                ('loginas', models.TextField(max_length=10, blank=True, null=True)),
                ('joinrequest', models.CharField(max_length=2, blank=True, null=True)),
                ('temp', models.CharField(max_length=2, blank=True, null=True)),
                ('ac', models.CharField(max_length=100, blank=True, null=True)),
                ('ifsc', models.CharField(max_length=100, blank=True, null=True)),
                ('paytm', models.CharField(max_length=100, blank=True, null=True)),
                ('upi', models.CharField(max_length=100, blank=True, null=True)),
                ('acname', models.CharField(max_length=100, blank=True, null=True)),
                ('bank', models.CharField(max_length=100, blank=True, null=True)),
                ('mode', models.CharField(max_length=100, blank=True, null=True)),
                ('contractor', models.PositiveSmallIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='contractor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

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
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('skill', models.CharField(max_length=100, null=True, blank=True)),
                ('nofworker', models.IntegerField(null=True, blank=True)),
                ('nameof_worker', models.CharField(max_length=1024, null=True, blank=True)),
                ('equipment', models.CharField(max_length=250, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('experience', models.CharField(max_length=250, null=True, blank=True)),
                ('description1', models.TextField(max_length=250, null=True, blank=True)),
                ('description2', models.TextField(max_length=100, null=True, blank=True)),
                ('dis', models.FloatField(null=True, blank=True)),
                ('joinrequest', models.CharField(max_length=2, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Current_location',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('address', models.CharField(max_length=250, null=True, blank=True)),
                ('lat', models.CharField(max_length=50, null=True, blank=True)),
                ('lng', models.CharField(max_length=50, null=True, blank=True)),
                ('time', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('username', models.CharField(primary_key=True, max_length=50, serialize=False)),
                ('lat', models.CharField(max_length=50, null=True, blank=True)),
                ('lng', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('s_contact', models.CharField(max_length=50, null=True, blank=True)),
                ('dis', models.FloatField(null=True, blank=True)),
                ('street', models.CharField(max_length=250, null=True, blank=True)),
                ('address', models.CharField(max_length=250, null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('skill1', models.CharField(max_length=100, null=True, blank=True)),
                ('skill2', models.CharField(max_length=100, null=True, blank=True)),
                ('skill3', models.CharField(max_length=100, null=True, blank=True)),
                ('description1', models.TextField(max_length=250, null=True, blank=True)),
                ('description2', models.TextField(max_length=250, null=True, blank=True)),
                ('description3', models.TextField(max_length=250, null=True, blank=True)),
                ('description', models.TextField(max_length=500, null=True, blank=True)),
                ('description11', models.TextField(max_length=250, null=True, blank=True)),
                ('min_salary', models.IntegerField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('nhirer', models.IntegerField(null=True, blank=True)),
                ('loginas', models.TextField(max_length=10, null=True, blank=True)),
                ('joinrequest', models.CharField(max_length=2, null=True, blank=True)),
                ('temp', models.CharField(max_length=2, null=True, blank=True)),
                ('ac', models.CharField(max_length=100, null=True, blank=True)),
                ('ifsc', models.CharField(max_length=100, null=True, blank=True)),
                ('paytm', models.CharField(max_length=100, null=True, blank=True)),
                ('upi', models.CharField(max_length=100, null=True, blank=True)),
                ('acname', models.CharField(max_length=100, null=True, blank=True)),
                ('bank', models.CharField(max_length=100, null=True, blank=True)),
                ('mode', models.CharField(max_length=100, null=True, blank=True)),
                ('contractor', models.PositiveSmallIntegerField(default=0, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='contractor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('cid', models.AutoField(serialize=False, primary_key=True)),
<<<<<<< HEAD
                ('skill', models.CharField(null=True, max_length=100, blank=True)),
                ('nofworker', models.IntegerField(null=True, blank=True)),
                ('nameof_worker', models.CharField(null=True, max_length=1024, blank=True)),
                ('equipment', models.CharField(null=True, max_length=250, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('experience', models.CharField(null=True, max_length=250, blank=True)),
                ('description1', models.TextField(null=True, max_length=250, blank=True)),
                ('description2', models.TextField(null=True, max_length=100, blank=True)),
                ('dis', models.FloatField(null=True, blank=True)),
                ('joinrequest', models.CharField(null=True, max_length=2, blank=True)),
=======
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
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
            ],
        ),
        migrations.CreateModel(
            name='Current_location',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('address', models.CharField(null=True, max_length=250, blank=True)),
                ('lat', models.CharField(null=True, max_length=50, blank=True)),
                ('lng', models.CharField(null=True, max_length=50, blank=True)),
                ('time', models.CharField(null=True, max_length=50, blank=True)),
=======
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=250, blank=True, null=True)),
                ('lat', models.CharField(max_length=50, blank=True, null=True)),
                ('lng', models.CharField(max_length=50, blank=True, null=True)),
                ('time', models.CharField(max_length=50, blank=True, null=True)),
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
<<<<<<< HEAD
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('lat', models.CharField(null=True, max_length=50, blank=True)),
                ('lng', models.CharField(null=True, max_length=50, blank=True)),
=======
                ('username', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('lat', models.CharField(max_length=50, blank=True, null=True)),
                ('lng', models.CharField(max_length=50, blank=True, null=True)),
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
<<<<<<< HEAD
                ('user', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('s_contact', models.CharField(null=True, max_length=50, blank=True)),
                ('dis', models.FloatField(null=True, blank=True)),
                ('street', models.CharField(null=True, max_length=250, blank=True)),
                ('address', models.CharField(null=True, max_length=250, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('skill1', models.CharField(null=True, max_length=100, blank=True)),
                ('skill2', models.CharField(null=True, max_length=100, blank=True)),
                ('skill3', models.CharField(null=True, max_length=100, blank=True)),
                ('description1', models.TextField(null=True, max_length=250, blank=True)),
                ('description2', models.TextField(null=True, max_length=250, blank=True)),
                ('description3', models.TextField(null=True, max_length=250, blank=True)),
                ('description', models.TextField(null=True, max_length=500, blank=True)),
                ('description11', models.TextField(null=True, max_length=250, blank=True)),
                ('min_salary', models.IntegerField(null=True, blank=True)),
                ('rating', models.FloatField(null=True, blank=True)),
                ('nhirer', models.IntegerField(null=True, blank=True)),
                ('loginas', models.TextField(null=True, max_length=10, blank=True)),
                ('joinrequest', models.CharField(null=True, max_length=2, blank=True)),
                ('temp', models.CharField(null=True, max_length=2, blank=True)),
                ('ac', models.CharField(null=True, max_length=100, blank=True)),
                ('ifsc', models.CharField(null=True, max_length=100, blank=True)),
                ('paytm', models.CharField(null=True, max_length=100, blank=True)),
                ('upi', models.CharField(null=True, max_length=100, blank=True)),
                ('acname', models.CharField(null=True, max_length=100, blank=True)),
                ('bank', models.CharField(null=True, max_length=100, blank=True)),
                ('mode', models.CharField(null=True, max_length=100, blank=True)),
                ('contractor', models.PositiveSmallIntegerField(null=True, default=0, blank=True)),
=======
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
>>>>>>> c857855f64a4d26416915fc5bf797649f8eb9416
            ],
        ),
        migrations.AddField(
            model_name='contractor',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]

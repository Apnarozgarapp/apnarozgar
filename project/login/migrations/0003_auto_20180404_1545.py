# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='pay',
            new_name='pmode',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='feedback',
            name='status',
        ),
        migrations.AddField(
            model_name='feedback',
            name='description',
            field=models.TextField(blank=True, null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback1',
            field=models.TextField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback2',
            field=models.TextField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='feedback3',
            field=models.TextField(blank=True, null=True, max_length=100),
        ),
        migrations.AddField(
            model_name='feedback',
            name='pdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]

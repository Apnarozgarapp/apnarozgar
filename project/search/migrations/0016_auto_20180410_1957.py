# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0015_auto_20180406_1359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='temp1',
            new_name='target',
        ),
    ]

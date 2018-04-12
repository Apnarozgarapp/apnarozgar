# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20180412_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contractor',
            old_name='key',
            new_name='user',
        ),
    ]

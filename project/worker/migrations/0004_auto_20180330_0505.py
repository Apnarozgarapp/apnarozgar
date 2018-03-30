# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0003_auto_20180330_0446'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='joinrequst',
            new_name='joinrequest',
        ),
    ]

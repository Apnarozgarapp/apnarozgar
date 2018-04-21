# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_loginas'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LoginAs',
        ),
    ]

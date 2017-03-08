# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_auto_20160801_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.PositiveIntegerField(default=160),
        ),
    ]

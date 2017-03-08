# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_product_nickname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='qty',
        ),
        migrations.AddField(
            model_name='product',
            name='year',
            field=models.PositiveIntegerField(default=2016),
        ),
    ]

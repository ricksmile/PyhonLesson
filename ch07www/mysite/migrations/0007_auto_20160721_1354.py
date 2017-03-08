# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_product_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brand',
            new_name='Maker',
        ),
    ]

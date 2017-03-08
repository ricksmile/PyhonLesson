# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_pmodel_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=b'\xe6\x9a\xab\xe7\x84\xa1\xe8\xaa\xaa\xe6\x98\x8e'),
        ),
    ]

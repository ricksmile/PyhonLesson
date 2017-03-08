# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_auto_20160721_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='pphoto',
            name='description',
            field=models.CharField(default=b'\xe7\x94\xa2\xe5\x93\x81\xe7\x85\xa7\xe7\x89\x87', max_length=20),
        ),
    ]

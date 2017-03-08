# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='nickname',
            field=models.CharField(default=b'\xe8\xb6\x85\xe5\x80\xbc\xe4\xba\x8c\xe6\x89\x8b\xe6\xa9\x9f', max_length=15),
        ),
    ]

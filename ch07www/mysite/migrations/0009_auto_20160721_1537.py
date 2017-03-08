# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_pphoto_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pmodel',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_profile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.PositiveIntegerField(default=160),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='male',
            field=models.BooleanField(default=False),
        ),
    ]

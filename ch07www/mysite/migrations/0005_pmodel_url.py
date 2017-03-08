# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_pphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='pmodel',
            name='url',
            field=models.URLField(default=b'http://i.imgur.com/Ous4iGB.png'),
        ),
    ]

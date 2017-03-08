# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20160720_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='PPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(default=b'http://i.imgur.com/Z230eeq.png')),
                ('product', models.ForeignKey(to='mysite.Product')),
            ],
        ),
    ]

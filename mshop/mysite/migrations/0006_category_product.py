# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20160819_0940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.URLField(null=True)),
                ('website', models.URLField(null=True)),
                ('stock', models.PositiveIntegerField(default=0)),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('category', models.ForeignKey(to='mysite.Category')),
            ],
        ),
    ]

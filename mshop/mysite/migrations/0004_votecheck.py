# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_auto_20160816_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoteCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.PositiveIntegerField()),
                ('pollid', models.PositiveIntegerField()),
                ('vote_date', models.DateField()),
            ],
        ),
    ]

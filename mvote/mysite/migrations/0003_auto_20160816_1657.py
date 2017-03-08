# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_poll_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggeduser',
            name='user',
        ),
        migrations.DeleteModel(
            name='LoggedUser',
        ),
    ]

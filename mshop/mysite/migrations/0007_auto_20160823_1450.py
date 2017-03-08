# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_category_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='product_image', to=b'filer.Image'),
        ),
    ]

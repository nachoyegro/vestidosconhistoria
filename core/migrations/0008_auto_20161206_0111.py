# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_vendetuvestidoimagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vestidoimagen',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media', blank=True),
        ),
    ]

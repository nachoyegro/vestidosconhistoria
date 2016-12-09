# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0004_auto_20161204_0837'),
        ('core', '0009_auto_20161206_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='VestidosManager',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.Content')),
                ('vestidos', models.ManyToManyField(to='core.Vestido')),
            ],
            bases=('webpage_core.content',),
        ),
    ]

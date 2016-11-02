# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0003_auto_20160220_1220'),
        ('core', '0005_auto_20161018_2224'),
    ]

    operations = [
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('simpletext_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.SimpleText')),
            ],
            bases=('webpage_core.simpletext',),
        ),
    ]

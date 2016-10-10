# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0003_auto_20160220_1220'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderContent',
            fields=[
                ('imagetextcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.ImageTextContent')),
            ],
            bases=('webpage_core.imagetextcontent',),
        ),
    ]

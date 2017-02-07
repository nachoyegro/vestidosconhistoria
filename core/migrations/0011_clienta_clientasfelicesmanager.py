# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0004_auto_20161204_0837'),
        ('core', '0010_vestidosmanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clienta',
            fields=[
                ('imagetextcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.ImageTextContent')),
            ],
            bases=('webpage_core.imagetextcontent',),
        ),
        migrations.CreateModel(
            name='ClientasFelicesManager',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.Content')),
                ('clientas', models.ManyToManyField(to='core.Clienta')),
            ],
            bases=('webpage_core.content',),
        ),
    ]

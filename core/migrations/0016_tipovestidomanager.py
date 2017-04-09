# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0004_auto_20161204_0837'),
        ('core', '0015_imagenportada'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoVestidoManager',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.Content')),
                ('tipos', models.ManyToManyField(to='core.TipoVestido')),
            ],
            bases=('webpage_core.content',),
        ),
    ]

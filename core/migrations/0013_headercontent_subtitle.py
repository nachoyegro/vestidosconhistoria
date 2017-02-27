# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170208_1919'),
    ]

    operations = [
        migrations.AddField(
            model_name='headercontent',
            name='subtitle',
            field=tinymce.models.HTMLField(default='', verbose_name='Subtitulo'),
            preserve_default=False,
        ),
    ]

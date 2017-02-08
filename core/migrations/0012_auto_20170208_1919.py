# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_clienta_clientasfelicesmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Respuesta'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='question',
            field=tinymce.models.HTMLField(verbose_name='Pregunta'),
        ),
    ]

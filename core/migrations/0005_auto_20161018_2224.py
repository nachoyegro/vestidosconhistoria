# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_vendetuvestido'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacto',
            old_name='mensaje',
            new_name='comentario',
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='asunto',
            new_name='conocieron',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='localidad',
        ),
        migrations.RemoveField(
            model_name='contacto',
            name='provincia',
        ),
        migrations.AddField(
            model_name='contacto',
            name='fecha_casamiento',
            field=models.DateField(null=True, blank=True),
        ),
    ]

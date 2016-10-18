# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_botonera'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendeTuVestido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=64, null=True, blank=True)),
                ('fecha_casamiento', models.DateField()),
                ('modista', models.CharField(max_length=255)),
                ('precio_venta', models.DecimalField(max_digits=10, decimal_places=2)),
                ('talle_contorno_espalda', models.CharField(max_length=128)),
                ('talle_corpino', models.CharField(max_length=128)),
                ('altura', models.CharField(max_length=128)),
                ('comentarios', models.TextField()),
            ],
        ),
    ]

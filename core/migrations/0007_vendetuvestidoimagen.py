# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_texto'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendeTuVestidoImagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to='images', blank=True)),
                ('vestido', models.ForeignKey(related_name='imagenes', to='core.VendeTuVestido')),
            ],
        ),
    ]

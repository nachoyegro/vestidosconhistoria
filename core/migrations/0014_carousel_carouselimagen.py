# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0004_auto_20161204_0837'),
        ('core', '0013_headercontent_subtitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.Content')),
            ],
            bases=('webpage_core.content',),
        ),
        migrations.CreateModel(
            name='CarouselImagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to='images', blank=True)),
                ('texto', models.TextField(null=True, blank=True)),
                ('carousel', models.ForeignKey(related_name='imagenes', to='core.Carousel')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpage_core', '0003_auto_20160220_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=64, null=True, blank=True)),
                ('provincia', models.CharField(max_length=128, null=True, blank=True)),
                ('localidad', models.CharField(max_length=128, null=True, blank=True)),
                ('asunto', models.CharField(max_length=255)),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.Content')),
                ('content', models.TextField(verbose_name='Respuesta')),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
            bases=('webpage_core.content',),
        ),
        migrations.CreateModel(
            name='TextoYFoto',
            fields=[
                ('imagetextcontent_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.ImageTextContent')),
            ],
            bases=('webpage_core.imagetextcontent',),
        ),
        migrations.CreateModel(
            name='TipoVestido',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField(verbose_name='Pregunta')),
            ],
        ),
        migrations.CreateModel(
            name='Vestido',
            fields=[
                ('simpletext_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='webpage_core.SimpleText')),
                ('tipo', models.ForeignKey(to='core.TipoVestido')),
            ],
            bases=('webpage_core.simpletext',),
        ),
        migrations.CreateModel(
            name='VestidoImagen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imagen', models.ImageField(null=True, upload_to='images', blank=True)),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
                ('index', models.IntegerField(null=True, verbose_name='\xcdndice', blank=True)),
                ('vestido', models.ForeignKey(related_name='imagenes', to='core.Vestido')),
            ],
        ),
        migrations.AddField(
            model_name='faq',
            name='topic',
            field=models.ForeignKey(to='core.Topic'),
        ),
    ]

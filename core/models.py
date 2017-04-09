#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from webpage_core.models import SimpleText, ImageTextContent, Content
from tinymce.models import HTMLField

class TextoYFoto(ImageTextContent):
    def __unicode__(self):
        return u'Texto y foto: %s' % (self.title)

class ImagenPortada(ImageTextContent):
    def __unicode__(self):
        return u'Imagen de portada'

    def get_template_name(self):
        return 'imagen_portada.html'

class TipoVestido(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.nombre

class Texto(SimpleText):
    def __unicode__(self):
        return u'Texto: %s' % (self.title)

# Create your models here.
# ImageTextContent es un tipo de Content, que tiene una Imagen, texto y un titulo.
# Es necesario que Product herede de eso para poder agregarle un precio
class Vestido(SimpleText):
    tipo = models.ForeignKey(TipoVestido)

    def get_template_name(self):
        return 'vestido_content.html'

    def get_template_preview_name(self):
        return 'vestido_preview.html'

    def get_context(self, **kwargs):
        #Me traigo el context de SimpleText
        context = super(Vestido, self).get_context(**kwargs)
        #Le agrego el precio
        context['imagenes'] = self.imagenes.all().order_by('index')
        context['id'] = self.pk
        context['tipo'] = self.tipo
        context['consulta'] = kwargs.get('consulta', False)
        return context

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.title, self.tipo)

class VestidoImagen(models.Model):
    vestido = models.ForeignKey(Vestido, related_name='imagenes')
    imagen = models.ImageField(blank=True, null=True, upload_to='images')
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    index = models.IntegerField(verbose_name='Índice', blank=True, null=True)

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.vestido,self.descripcion)

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=64, blank=True, null=True)
    fecha_casamiento = models.DateField(blank=True, null=True)
    conocieron = models.CharField(max_length=255)
    comentario = models.TextField()

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.nombre, self.fecha_casamiento)

class Topic(models.Model):
    question = HTMLField('Pregunta')

    def __unicode__(self):
        return u'%s' % self.question

class FAQ(Content):
    topic = models.ForeignKey(Topic)
    content = HTMLField('Respuesta')
    order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.topic

    def get_context(self, **kwargs):
        context = {}
        context['topic'] = self.topic
        context['content'] = self.content
        return context

    def get_template_name(self):
        return 'faq.html'

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'

class HeaderContent(ImageTextContent):
    subtitle = HTMLField('Subtitulo')

    def get_context(self, **kwargs):
        context = super(HeaderContent, self).get_context(**kwargs)
        context['subtitulo'] = self.subtitle
        return context

    def get_template_name(self):
        return 'header.html'

    def __unicode__(self, *args, **kwargs):
        return u"%s" % self.title

class Botonera(Content):

    def get_template_name(self):
        return 'botonera.html'

    def __unicode__(self, *args, **kwargs):
        return u'Botonera'

class Carousel(Content):

    def get_context(self, **kwargs):
        context = {}
        context['imagenes'] = self.imagenes.all()
        return context

    def get_template_name(self):
        return 'carousel.html'

    def __unicode__(self, *args, **kwargs):
        return u'Carousel'

class CarouselImagen(models.Model):
    carousel = models.ForeignKey(Carousel, related_name='imagenes')
    imagen = models.ImageField(blank=True, null=True, upload_to='images')
    texto = models.TextField(blank=True, null=True)


class VendeTuVestido(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=64, blank=True, null=True)
    fecha_casamiento = models.DateField()
    modista = models.CharField(max_length=255)
    precio_venta = models.DecimalField(decimal_places=2, max_digits=10)
    talle_contorno_espalda = models.CharField(max_length=128)
    talle_corpino = models.CharField(max_length=128)
    altura = models.CharField(max_length=128)
    comentarios = models.TextField()

    def __unicode__(self, *args, **kwargs):
        return u'%s-%s' % (self.nombre, self.apellido)


class VendeTuVestidoImagen(models.Model):
    vestido = models.ForeignKey(VendeTuVestido, related_name='imagenes')
    imagen = models.ImageField(blank=True, null=True, upload_to='images')

    def __unicode__(self, *args, **kwargs):
        return u"%s" % (self.vestido)

#Este es un content nuevo, que reune muchos vestidos
class VestidosManager(Content):
    vestidos = models.ManyToManyField(Vestido)

    def __unicode__(self, *args, **kwargs):
        return u'Soy un conjunto de vestidos'

    def get_template_name(self):
        return 'vestidos_manager.html'

    def get_context(self, **kwargs):
        vestidos_pks = kwargs.get('pks', None)
        if vestidos_pks:
            vestidos = self.vestidos.filter(pk__in=vestidos_pks)
        else:
            vestidos = self.vestidos.all()
        context = {}
        context['vestidos'] = [vestido.get_preview_html() for vestido in vestidos]
        return context

class Clienta(ImageTextContent):

    def __unicode__(self, *args, **kwargs):
        return u'Clienta: %s' % (self.title)

    def get_template_preview_name(self):
        return 'clienta_preview.html'

    def get_context(self, **kwargs):
        #Me traigo el context de SimpleText
        context = super(Clienta, self).get_context(**kwargs)
        context['imagen'] = self.image
        context['id'] = self.pk
        return context

#Este es un content nuevo, que reune muchas clientas
class ClientasFelicesManager(Content):
    clientas = models.ManyToManyField(Clienta)

    def __unicode__(self, *args, **kwargs):
        return u'Clientas'

    def get_template_name(self):
        return 'clientas_manager.html'

    def get_context(self, **kwargs):
        clientas_pks = kwargs.get('pks', None)
        if clientas_pks:
            clientas = self.clientas.filter(pk__in=clientas_pks)
        else:
            clientas = self.clientas.all()
        context = {}
        context['clientas'] = [clienta.get_preview_html() for clienta in clientas]
        return context

class TipoVestidoManager(Content):
    tipos = models.ManyToManyField(TipoVestido)

    def __unicode__(self, *args, **kwargs):
        return u'Tipos'

    def get_template_name(self):
        return 'tipos_manager.html'

    def get_context(self, **kwargs):
        context = {}
        context['tipos'] = self.tipos.all()
        return context

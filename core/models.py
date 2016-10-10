#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from webpage_core.models import SimpleText, ImageTextContent, Content

class TextoYFoto(ImageTextContent):
    def __unicode__(self):
        return u'Texto y foto: %s' % (self.title)

class TipoVestido(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s' % self.nombre

# Create your models here.
# ImageTextContent es un tipo de Content, que tiene una Imagen, texto y un titulo.
# Es necesario que Product herede de eso para poder agregarle un precio
class Vestido(SimpleText):
    tipo = models.ForeignKey(TipoVestido)

    def get_template_name(self):
        return 'vestido.html'

    def get_context(self):
        #Me traigo el context de SimpleText
        context = super(Vestido, self).get_context()
        #Le agrego el precio
        context['imagenes'] = self.imagenes.all().order_by('index')
        context['id'] = self.pk
        return context

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.title, self.tipo)

class VestidoImagen(models.Model):
    vestido = models.ForeignKey(Vestido, related_name='imagenes')
    imagen = models.ImageField(blank=True, null=True, upload_to='images')
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    index = models.IntegerField(verbose_name='Índice', blank=True, null=True)

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.product,self.description)

class Contacto(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telefono = models.CharField(max_length=64, blank=True, null=True)
    provincia = models.CharField(max_length=128, blank=True, null=True)
    localidad = models.CharField(max_length=128, blank=True, null=True)
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.nombre, self.asunto)

class Topic(models.Model):
    question = models.TextField('Pregunta')

    def __unicode__(self):
        return u'%s' % self.question

class FAQ(Content):
    topic = models.ForeignKey(Topic)
    content = models.TextField('Respuesta')
    order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.topic

    def get_context(self):
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

    def get_template_name(self):
        return 'header.html'

    def __unicode__(self, *args, **kwargs):
        return u"%s" % self.title

class Botonera(Content):

    def get_template_name(self):
        return 'botonera.html'

    def __unicode__(self, *args, **kwargs):
        return u'Botonera'

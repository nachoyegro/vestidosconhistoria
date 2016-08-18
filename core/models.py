from __future__ import unicode_literals

from django.db import models

# Create your models here.
# ImageTextContent es un tipo de Content, que tiene una Imagen, texto y un titulo.
# Es necesario que Product herede de eso para poder agregarle un precio
class Vestido(SimpleText):

    def get_template_name(self):
        return 'product.html'

    def get_context(self):
        #Me traigo el context de SimpleText
        context = super(Product, self).get_context()
        #Le agrego el precio
        context['price'] = self.price
        context['items'] = self.items.all().order_by('index')
        context['id'] = self.pk
        context['disponibilidad'] = self.disponibilidad
        return context

    def __unicode__(self, *args, **kwargs):
        return u"%s %s" % (self.title, str(self.price))

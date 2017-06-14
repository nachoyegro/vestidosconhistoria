from django.contrib import admin
from core.models import *
from django.db import models
from django import forms

class VestidoImagenInline(admin.TabularInline):
    model = VestidoImagen

class VestidoAdmin(admin.ModelAdmin):
    inlines = [VestidoImagenInline, ]
    exclude = ['pages', 'is_global']
    list_display = ['title', 'tipo']

class VendeTuVestidoImagenInline(admin.TabularInline):
    model = VendeTuVestidoImagen

class VendeTuVestidoAdmin(admin.ModelAdmin):
    inlines = [VendeTuVestidoImagenInline, ]
    readonly_fields = ['nombre', 'apellido', 'email', 'telefono', 'fecha_casamiento', 'modista',
     'precio_venta', 'talle_contorno_espalda', 'talle_corpino', 'medida_cintura', 'medida_cadera', 'altura', 'comentarios']

class HTMLTextAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)

class TextoAdmin(HTMLTextAdmin):
    exclude = ['is_global']

class HeaderContentAdmin(HTMLTextAdmin):
    pass

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fecha_casamiento']
    readonly_fields = ['nombre', 'email', 'telefono', 'fecha_casamiento', 'conocieron', 'comentario']

class FAQAdmin(HTMLTextAdmin):
    exclude = ['is_global', 'order']

class TextoYFotoAdmin(HTMLTextAdmin):
    exclude = ['is_global']
    pass

class ClientaAdmin(admin.ModelAdmin):
    exclude = ['pages',]

class TopicAdmin(HTMLTextAdmin):
    pass

class CarouselImagenInline(admin.TabularInline):
    model = CarouselImagen

class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselImagenInline, ]


# Register your models here.
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(Vestido, VestidoAdmin)
admin.site.register(TipoVestido)
admin.site.register(TextoYFoto, TextoYFotoAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(HeaderContent, HeaderContentAdmin)
admin.site.register(Botonera)
admin.site.register(ImagenPortada)
admin.site.register(Texto, TextoAdmin)
admin.site.register(VendeTuVestido, VendeTuVestidoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(VestidosManager)
admin.site.register(TipoVestidoManager)
admin.site.register(ClientasFelicesManager)
admin.site.register(Clienta, ClientaAdmin)

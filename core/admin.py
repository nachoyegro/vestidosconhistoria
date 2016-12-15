from django.contrib import admin
from core.models import *
from django.db import models
from django import forms

class VestidoImagenInline(admin.TabularInline):
    model = VestidoImagen

class VestidoAdmin(admin.ModelAdmin):
    inlines = [VestidoImagenInline, ]
    exclude = ['pages',]
    list_display = ['title', 'tipo']

class VendeTuVestidoImagenInline(admin.TabularInline):
    model = VendeTuVestidoImagen

class VendeTuVestidoAdmin(admin.ModelAdmin):
    inlines = [VendeTuVestidoImagenInline, ]

class HTMLTextAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)

class TextoAdmin(HTMLTextAdmin):
    pass

class HeaderContentAdmin(HTMLTextAdmin):
    pass

class ContactoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'fecha_casamiento']

# Register your models here.
admin.site.register(Vestido, VestidoAdmin)
admin.site.register(TipoVestido)
admin.site.register(TextoYFoto)
admin.site.register(Topic)
admin.site.register(FAQ)
admin.site.register(HeaderContent, HeaderContentAdmin)
admin.site.register(Botonera)
admin.site.register(Texto, TextoAdmin)
admin.site.register(VendeTuVestido, VendeTuVestidoAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(VestidosManager)

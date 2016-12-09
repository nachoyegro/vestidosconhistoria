from django.contrib import admin
from core.models import *

class VestidoImagenInline(admin.TabularInline):
    model = VestidoImagen

class VestidoAdmin(admin.ModelAdmin):
    inlines = [VestidoImagenInline, ]
    exclude = ['pages',]

class VendeTuVestidoImagenInline(admin.TabularInline):
    model = VendeTuVestidoImagen

class VendeTuVestidoAdmin(admin.ModelAdmin):
    inlines = [VendeTuVestidoImagenInline, ]

# Register your models here.
admin.site.register(Vestido, VestidoAdmin)
admin.site.register(TipoVestido)
admin.site.register(TextoYFoto)
admin.site.register(Topic)
admin.site.register(FAQ)
admin.site.register(HeaderContent)
admin.site.register(Botonera)
admin.site.register(Texto)
admin.site.register(VendeTuVestido, VendeTuVestidoAdmin)
admin.site.register(Contacto)
admin.site.register(VestidosManager)

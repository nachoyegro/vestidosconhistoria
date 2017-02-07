from django.db.models.signals import pre_save, post_save, post_delete
from PIL import Image
from cStringIO import StringIO

def compress_image(sender, instance, created,**kwargs):
    if created:
        compress(instance.imagen.path)

def compress(image):
    # Open the image
    im = Image.open(image)
    # Now save it
    im.save(image, format="JPEG", quality=50)
    return im

def nuevo_vestido(sender, instance, created, **kwargs):
    if created:
        from core.models import VestidosManager
        manager = VestidosManager.objects.all()[0]
        manager.vestidos.add(instance)
        manager.save()

def nueva_clienta(sender, instance, created, **kwargs):
    if created:
        from core.models import ClientasFelicesManager
        manager = ClientasFelicesManager.objects.all()[0]
        manager.clientas.add(instance)
        manager.save()


post_save.connect(compress_image, sender='core.VestidoImagen', dispatch_uid='unique_compress')
post_save.connect(nuevo_vestido, sender='core.Vestido', dispatch_uid='unique_vestido')
post_save.connect(nueva_clienta, sender='core.Clienta', dispatch_uid='unique_clienta')

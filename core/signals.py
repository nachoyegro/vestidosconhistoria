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

post_save.connect(compress_image, sender='core.VestidoImagen', dispatch_uid='unique_compress')

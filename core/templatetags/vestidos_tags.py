from django import template
from webpage_core.models import Page
from core.models import Vestido
from itertools import chain
import string, unicodedata

register = template.Library()
table = string.maketrans("","")

@register.assignment_tag(takes_context=False)
def pages():
	return Page.objects.all().order_by('order')

@register.assignment_tag(takes_context=False)
def amount_of_pages():
	return Page.objects.all().count()

@register.assignment_tag(takes_context=False)
def cantidad_de_vestidos():
	return Vestido.objects.all().count()

@register.assignment_tag(takes_context=False)
def primer_pagina():
    try:
	   return Page.objects.all().order_by('order')[0]
    except:
        return None

def filter_punctuation(s):
    return str(s).translate(table, string.punctuation)

def remove_accents(data):
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if x in string.ascii_letters).lower()

def first_image(items):
    return items[0].imagen

def rest_images(items):
    return items[1:]

def first_image_title(items):
    return items[0].descripcion

def get_split(s):
    return filter_punctuation(remove_accents(s)).split(' ')[0]

def image_name(image):
	if not image.url:
		return None
    return image.url.split('/')[-1]

register.filter('pages', pages)
register.filter('primer_pagina', primer_pagina)
register.filter('image_name', image_name)
register.filter('get_split', get_split)
register.filter('first_image', first_image)
register.filter('rest_images', rest_images)
register.filter('first_image_title', first_image_title)

# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from webpage_core.models import Page, Content
from django.views.generic import View
from webpage_core.views import PageView
from core.forms import ContactForm, VendeTuVestidoForm
from django.http import HttpResponse, Http404, HttpResponseRedirect
from core.models import *
from buscador_vestidos import BuscadorVestidos
from django.db.models import Q
from django.core.mail import send_mail
import json
from django.conf import settings

# Create your views here.

def render_page(page, request, extras):
    contents = [content.get_html() for content in Content.objects.filter(pages=page).order_by('position').select_subclasses()]
    extras['contents'] = contents
    extras['title'] = page.title
    extras['background'] = page.background
    extras['success'] = request.GET.get('success', False)
    extras['error'] = request.GET.get('error', False)
    extras['asunto'] = request.GET.get('asunto', False)
    return render(request, page.html_name, extras)

class HomeView(View):

    def get(self, request):
        page = Page.objects.all().order_by('order')[0]
        return render_page(page, request, {})

class IndexView(View):

    def get(self, request):
        imagen1 = ImagenPortada.objects.all()[0]
        imagen2 = ImagenPortada.objects.all()[1]
        carousel = Carousel.objects.all()[0]
        botonera = Botonera.objects.all()[0]
        header = HeaderContent.objects.all()[0]
        return render(request, 'index.html', dict(header=header.get_html(), botonera=botonera.get_html() ,imagen1=imagen1.get_html(), imagen2=imagen2.get_html(), carousel=carousel.get_html()))

class ContactView(PageView):

    def get(self, request, extras = {}):
        page = get_object_or_404(Page, url_name='contacto')
        return render_page(page, request, extras)

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contacto = form.save()
            send_mail(
                'Se contactaron en Vestidos con Historia',
                'Para leer los datos ingrese aqui http://vestidosconhistoria.com/admin/core/contacto/%d/' % contacto.pk,
                'contacto.vestidosch@gmail.com',
                ['vestidosconhistoria@hotmail.com'],
                fail_silently=not settings.DEBUG,
            )
            return HttpResponseRedirect('/contacto/?success=True')
        return HttpResponseRedirect('/contacto/?error=True')

class VestidoView(View):
    def get(self, request, pk):
        vestido = get_object_or_404(Vestido, pk=pk)
        context = vestido.get_context(consulta=True)
        context['contents'] = [(content.get_html(), content.position) for content in Content.objects.filter(is_global=True).order_by('position').select_subclasses()]
        return render(request, 'vestido.html', context)

class VendeTuVestidoView(PageView):

    def get(self, request, extras = {}):
        page = get_object_or_404(Page, url_name='vende')
        return render_page(page, request, extras)

    def post(self, request, *args, **kwargs):
        form = VendeTuVestidoForm(data=request.POST)
        if form.is_valid():
            vestido = form.save()
            for imagen in dict(request.FILES)['images']:
                VendeTuVestidoImagen.objects.create(vestido=vestido, imagen=imagen)
            send_mail(
                'Cargaron un vestido en Vestidos con Historia!',
                'Para leerlo ingrese aquí http://vestidosconhistoria.com/admin/core/vendetuvestido/%s/' % str(vestido.pk),
                'contacto.vestidosch@gmail.com',
                ['vestidosconhistoria@hotmail.com', 'nachoyegro@gmail.com'],
                #['nachoyegro@gmail.com'],
                fail_silently=not settings.DEBUG, #Si estoy en produccion quiero que falle silenciosamente
            )
            return HttpResponseRedirect('/vende_tu_vestido/?success=True')
        return HttpResponseRedirect('/vende_tu_vestido/?error=True')

class VestidosFiltradosView(View):
    def get(self, request, *args, **kwargs):
        page = get_object_or_404(Page, url_name='vestidos')
        buscador_vestidos = BuscadorVestidos()
        vestidos = buscador_vestidos.get_vestidos(**request.GET)
        vestidos_pks = [vestido.pk for vestido in vestidos]
        contents = self.get_contents_with_order(vestidos_pks, page)
        return render(request, page.html_name, {'contents': contents, 'title': page.title, 'amount': len(contents)})

    def get_contents_with_order(self, contents_pks, page):
        contents = []
        #Aca busco el VestidoManager y los globales
        for content in Content.objects.filter(pages=page).order_by('position').select_subclasses():
            #Aca le digo al VestidoManager que tiene que filtrar por esos pks
            contents.append(content.get_html(pks=contents_pks))
        return contents

class NuevoComentarioView(View):
    def get(self, request, pk):
        send_mail(
            'Realizaron un comentario en Vestidos con Historia',
            'Para leerlo ingrese aquí http://vestidosconhistoria.com/vestido/%s/' % str(pk),
            'contacto.vestidosch@gmail.com',
            ['vestidosconhistoria@hotmail.com'],
            #['nachoyegro@gmail.com'],
            fail_silently=not settings.DEBUG, #Si estoy en produccion quiero que falle silenciosamente
        )
        return HttpResponse(json.dumps("success"))

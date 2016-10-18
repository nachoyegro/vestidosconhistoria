from django.shortcuts import render, redirect, get_object_or_404
from webpage_core.models import Page, Content
from django.views.generic import View
from webpage_core.views import PageView
from core.forms import ContactForm, VendeTuVestidoForm
from django.http import HttpResponse, Http404, HttpResponseRedirect


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

class ContactView(PageView):

    def get(self, request, extras = {}):
        page = get_object_or_404(Page, url_name='contacto')
        return render_page(page, request, extras)

    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/contacto/?success=True')
        return HttpResponseRedirect('/contacto/?error=True')

class VendeTuVestidoView(PageView):

    def get(self, request, extras = {}):
        page = get_object_or_404(Page, url_name='vende')
        return render_page(page, request, extras)

    def post(self, request, *args, **kwargs):
        form = VendeTuVestidoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vende_tu_vestido/?success=True')
        return HttpResponseRedirect('/vende_tu_vestido/?error=True')

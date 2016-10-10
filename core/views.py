from django.shortcuts import render, redirect, get_object_or_404
from webpage_core.models import Page, Content
from django.views.generic import View
from webpage_core.views import PageView

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
            to = get_list_mails()
            nombre = form['nombre'].data
            email = form['email'].data
            telefono = form['telefono'].data
            provincia = form['provincia'].data
            localidad = form['localidad'].data
            asunto = form['asunto'].data
            mensaje = form['mensaje'].data
            today = datetime.date.today()
            msg = '\n Ha recibido un mail de %s ' % nombre
            msg += 'con los siguientes datos: \n\n Email: %s' % email
            msg += '\n\n Telefono: %s' % telefono
            msg += '\n Provincia: %s' % provincia
            msg += '\n Localidad: %s' % localidad
            msg += '\n\n Mensaje: \n %s ' % mensaje
            msg += '\n\n\n Mensaje enviado desde vestidosconhistoria.com el %s' % today.strftime('%d/%m/%Y')
            try:
                send_mail(asunto, msg, email, to)
            except Exception as e:
                return HttpResponseRedirect('/contacto/?error=True')
            else:
                form.save()
                return HttpResponseRedirect('/contacto/?success=True')
        return HttpResponseRedirect('/contacto/?error=True')

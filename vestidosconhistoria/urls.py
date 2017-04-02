"""vestidosconhistoria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from core.views import IndexView, ContactView, VendeTuVestidoView, VestidoView, VestidosFiltradosView
from webpage_core.views import PageView
from django.conf import settings

urlpatterns = [
    url(r'^$', IndexView.as_view()),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
    url(r'^contacto/$', ContactView.as_view(), name='contact_view'),
    url(r'^vende_tu_vestido/$', VendeTuVestidoView.as_view(), name='vende_tu_vestido_view'),
    url(r'^vestido/(?P<pk>\w+)/$', VestidoView.as_view(), name='vestido_view'),
    url(r'^filtrados/(?P<url_name>\w+)/$', VestidosFiltradosView.as_view(), name='search_view'),
    url(r'^(?P<url_name>\w+)/', PageView.as_view(), name='page'),
]

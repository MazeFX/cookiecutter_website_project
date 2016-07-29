# -*- coding: utf-8 -*-

"""
File: urls.py
Creator: MazeFX
Date: 11-7-2016

Main url resolver as from cookiecutter-django.
Added following resolver patterns:

* ('/') -> pages.home_page
* ('/contact/') -> pages.contact_page
* ('/contact/email_sent/') -> pages.email_sent_page
"""


from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views

from website.pages import views as page_views

urlpatterns = [
    url(r'^$', page_views.home_page, name='home'),
    url(r'^contact/$', page_views.contact_page, name='contact'),
    url(r'^contact/email_sent/$', page_views.email_sent_page, name='email_sent'),
    url(r'^about/$', TemplateView.as_view(template_name='pages/about.html'), name='about'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, include(admin.site.urls)),

    # User management
    url(r'^users/', include('website.users.urls', namespace='users')),
    url(r'^accounts/', include('allauth.urls')),

    # Your stuff: custom urls includes go here

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]

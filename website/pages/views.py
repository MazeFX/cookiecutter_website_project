# -*- coding: utf-8 -*-

"""
File: pages/views.py
Creator: MazeFX
Date: 12-7-2016

Views written for rendering main website pages (home, about, contact, etc).
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from website.pages.forms import ContactForm


def home_page(request):
    return render(request, 'pages/home.html')


def contact_page(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['fullname'])
    return render(request, 'pages/contact.html', {'form': ContactForm()})

# -*- coding: utf-8 -*-

"""
File: pages/views.py
Creator: MazeFX
Date: 12-7-2016

Views written for rendering main website pages (home, about, contact, etc).
"""

from django.shortcuts import redirect, render
from django.core.mail import send_mail

from website.pages.forms import ContactForm


def home_page(request):
    return render(request, 'pages/home.html')


def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            print('-----------------------Form is valid___________')
            return redirect('../contact/mail_sent/')
    return render(request, 'pages/contact.html', {"form": form})

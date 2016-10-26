# -*- coding: utf-8 -*-

"""
File: pages/views.py
Creator: MazeFX
Date: 12-7-2016

Views written for rendering main website pages (home, about, contact, etc).
"""

from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from django.template.loader import get_template

from website.pages.forms import ContactForm


def home_page(request):
    return render(request, 'pages/home.html')

def home_page_old(request):
    return render(request, 'pages/home_old.html')

def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            reply_email = request.POST.get('email', '')
            template = get_template('pages/contact_email.txt')
            context = request.POST
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission from recruiter mail.",
                content,
                "MazeFXwebsite@Sandbox1164858fa1dc4ce7bf986ef9a82f17cb.Mailgun.Org",
                ['filoplast@gmail.com'],
                headers={'Reply-To': reply_email}
            )
            email.send()
            return redirect('../contact/email_sent/')
        return render(request, 'pages/contact.html', {"form": form})
    return render(request, 'pages/contact.html', {"form": form})


def email_sent_page(request):
    return render(request, 'pages/email_sent.html')

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


def contact_page(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            fullname = request.POST.get('fullname', '')
            email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')

            template = get_template('pages/contact_email.txt')
            context = {
                'fullname': fullname,
                'email': email,
                'subject': subject,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission from recruiter mail.",
                content,
                "MazeFXwebsite@contactform.com",
                ['filoplast@gmail.com'],
                headers={'Reply-To': email}
            )
            email.send()
            return redirect('../contact/mail_sent/')
        return render(request, 'pages/contact.html', {"form": form})
    return render(request, 'pages/contact.html', {"form": form})

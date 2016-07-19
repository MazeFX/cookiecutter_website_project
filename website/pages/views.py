# -*- coding: utf-8 -*-

"""
File: views.py
Creator: MazeFX
Date: 12-7-2016

Views written for rendering main website pages (home, about, contact, etc).
"""

from django.shortcuts import render
from django.core.mail import send_mail


def home_page(request):
    return render(request, 'pages/home.html')


def send_simple_message(request):
    return request.post(
        "https://api.mailgun.net/v3/Sandbox1164858fa1dc4ce7bf986ef9a82f17cb.Mailgun.Org/messages",
        auth=("api", "key-14bba8d2f8e7a762c300f608dce4e94f"),
        data={"from": "Excited User <mailgun@Sandbox1164858fa1dc4ce7bf986ef9a82f17cb.Mailgun.Org>",
              "to": ["filoplast@gmail.com", "YOU@Sandbox1164858fa1dc4ce7bf986ef9a82f17cb.Mailgun.Org"],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


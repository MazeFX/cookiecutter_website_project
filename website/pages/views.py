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

def send_email(request):
    send_mail("It works!", "This will get sent through Mailgun",
    "Anymail Mailgun says BOOM!!! <MazeFX@MazeFX.pythonanywhere.com>", ["filoplast@gmail.com"])
    return render(request, 'pages/about.html')


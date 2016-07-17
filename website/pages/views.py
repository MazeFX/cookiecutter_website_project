# -*- coding: utf-8 -*-

"""
File: views.py
Creator: MazeFX
Date: 12-7-2016

Views written for rendering main website pages (home, about, contact, etc).
"""

from django.shortcuts import render


def home_page(request):
    return render(request, 'pages/home.html')

# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: views.py
Creator: MazeFX
Date: 12-7-2016

Views written for rendering main website pages (home, about, contact, etc).
"""

from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<html><title>IT's my future</title></html>")

# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: tests.py
Creator: MazeFX
Date: 12-7-2016

Tests written for testing main website pages (home, about, contact, etc)
"""

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from website.pages.views import home_page


class HomePageTest(TestCase):

    # TODO - change home page from recruiter page to real home page

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('pages/home.html')

        self.assertEqual(response.content.decode(), expected_html)

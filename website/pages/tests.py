# -*- coding: utf-8 -*-

"""
File: tests.py
Creator: MazeFX
Date: 12-7-2016

Tests written for testing main website pages (home, about, contact, etc)

Contact page has the ability to send emails through anymail/mailgun.
"""

from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from website.pages.views import home_page, contact_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('pages/home.html')

        self.assertEqual(response.content.decode(), expected_html)


class ContactTest(TestCase):

    def test_contact_url_resolves_to_contact_page_view(self):
        found = resolve('/contact/')
        self.assertEqual(found.func, contact_page)

    def test_contact_page_returns_correct_html(self):
        request = HttpRequest()
        response = contact_page(request)
        expected_html = render_to_string('pages/contact.html', request=request)

        self.assertEqual(response.content.decode(), expected_html)

    def test_contact_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['fullname'] = 'Dave'

        response = contact_page(request)

        self.assertIn('Dave', response.content.decode())

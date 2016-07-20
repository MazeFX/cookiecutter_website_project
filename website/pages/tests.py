# -*- coding: utf-8 -*-

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

from website.pages.views import home_page, send_email


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('pages/home.html')

        self.assertEqual(response.content.decode(), expected_html)


class SendEmailTest(TestCase):

    def test_send_email_url_resolves_to_send_email_view(self):
        found = resolve('/send-email/')
        self.assertEqual(found.func, send_email)

    def test_send_email_returns_correct_html(self):
        request = HttpRequest()
        response = send_email(request)
        expected_html = render_to_string('pages/send_email.html')

        self.assertEqual(response.content.decode(), expected_html)

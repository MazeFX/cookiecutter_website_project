# -*- coding: utf-8 -*-

"""
File: pages/tests/test_views.py
Creator: MazeFX
Date: 12-7-2016

Tests written for testing main website pages (home, about, contact, etc)

Contact page has the ability to send emails through anymail/mailgun.
"""

from django.core.urlresolvers import resolve
from django.core import mail
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string, get_template
from django.utils.html import escape


from website.pages.views import home_page, home_page_old, coming_soon_page, contact_page, email_sent_page
from website.pages.forms import ContactForm, EMPTY_ITEM_ERROR


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('pages/home.html')

        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'pages/home.html')


class HomePageOldTest(TestCase):

    def test_home_old_url_resolves_to_home_page_old_view(self):
        found = resolve('/home_old/')
        self.assertEqual(found.func, home_page_old)

    def test_home_page_old_returns_correct_html(self):
        request = HttpRequest()
        response = home_page_old(request)
        expected_html = render_to_string('pages/home_old.html')

        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_old_renders_home_template(self):
        response = self.client.get('/home_old/')

        self.assertTemplateUsed(response, 'pages/home_old.html')


class ComingSoonTest(TestCase):

    def test_coming_soon_url_resolves_to_coming_soon_page_view(self):
        found = resolve('/portfolio/coming_soon/')
        self.assertEqual(found.func, coming_soon_page)

    def test_coming_soon_page_returns_correct_html(self):
        request = HttpRequest()
        response = coming_soon_page(request)
        expected_html = render_to_string('pages/coming_soon.html')

        self.assertEqual(response.content.decode(), expected_html)

    def test_coming_soon_page_renders_coming_soon_template(self):
        response = self.client.get('/portfolio/coming_soon/')

        self.assertTemplateUsed(response, 'pages/coming_soon.html')


class ContactTest(TestCase):

    TEST_POST = {'fullname': 'Dave',
                 'email': 'from@MazeFXtester.com',
                 'subject': 'Unit test mail',
                 'message': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum et purus '
                            'interdum dui auctor tempus eget vel sapien. Etiam in.'
                 }

    def test_contact_url_resolves_to_contact_page_view(self):
        found = resolve('/contact/')

        self.assertEqual(found.func, contact_page)

    def test_contact_page_renders_contact_template(self):
        response = self.client.get('/contact/')

        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_contact_page_uses_contact_form(self):
        response = self.client.get('/contact/')

        self.assertIsInstance(response.context['form'], ContactForm)

    def test_for_invalid_input_renders_contact_template(self):
        response = self.client.post('/contact/', data={'fullname': ''})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/contact.html')

    def test_validation_errors_are_shown_on_contact_page(self):
        response = self.client.post('/contact/', data={'fullname': ''})

        self.assertContains(response, escape(EMPTY_ITEM_ERROR))

    def test_for_invalid_input_passes_form_to_template(self):
        response = self.client.post('/contact/', data={'fullname': ''})

        self.assertIsInstance(response.context['form'], ContactForm)

    def test_contact_page_returns_a_POST_request_on_submit(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['fullname'] = 'Dave'

        response = contact_page(request)

        self.assertIn('Dave', response.content.decode())

    def test_contact_page_sends_an_email_on_submit(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = self.TEST_POST

        response = contact_page(request)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'New contact form submission from recruiter mail.')

    def test_sent_email_uses_correct_email_template(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = self.TEST_POST

        template = get_template('pages/contact_email.txt')
        context = self.TEST_POST

        content = template.render(context)
        response = contact_page(request)

        self.assertEqual(mail.outbox[0].body, content)


class EmailSentPageTest(TestCase):

    def test_root_url_resolves_to_email_sent_page_view(self):
        found = resolve('/contact/email_sent/')
        self.assertEqual(found.func, email_sent_page)

    def test_email_sent_page_returns_correct_html(self):
        request = HttpRequest()
        response = email_sent_page(request)
        expected_html = render_to_string('pages/email_sent.html')
        self.assertMultiLineEqual(response.content.decode(), expected_html)

    def test_email_sent_renders_email_sent_template(self):
        response = self.client.get('/contact/email_sent/')

        self.assertTemplateUsed(response, 'pages/email_sent.html')

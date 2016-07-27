# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: pages/tests/test_forms.py
Creator: MazeFX
Date: 26-7-2016

Python Test docstring.
"""

from django.test import TestCase
from website.pages.forms import ContactForm

from website.pages.forms import EMPTY_ITEM_ERROR, EMAIL_FORMAT_ERROR


class ContactFormTest(TestCase):

    def test_form_renders_all_text_input(self):
        form = ContactForm()
        self.assertIn('id="id_fullname"', form.as_p())
        # TODO - add other field too

    def test_form_validation_for_blank_fields(self):
        form = ContactForm(data={'fullname': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['fullname'], [EMPTY_ITEM_ERROR])

    def test_form_validation_for_email(self):
        form = ContactForm(data={'email': 'not an email'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [EMAIL_FORMAT_ERROR])
        # TODO - add other field too


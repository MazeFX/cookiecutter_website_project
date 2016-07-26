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


class ItemFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = ContactForm()
        self.fail(form.as_p())

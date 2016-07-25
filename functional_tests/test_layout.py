# -*- coding: utf-8 -*-

"""
File: functional/test_layout.py
Creator: MazeFX
Date: 25-7-2016

1st functional test construct written by following the book
'Test Driven Development with Python' by Harry Percival.
Thanks Harry for giving me a guideline to becoming a good developer.

User description:
-----------------

Name: Dave
Occupation: Recruiter for a Django company
Goal: Recruit a Django Developer who is enthusiastic about programming
      and has shown that he is prepared to obey the testing goat.

"""

from .base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):

    def test_layout_and_styling(self):

        # Dave goes to the recruiter page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # He notices the header title has a nice font
        header_title = self.browser.find_element_by_id('header-title-begin')
        header_font = header_title.value_of_css_property('font-family')

        self.assertIn('Droid Sans', header_font)

        # Dave is satisfied with the knowledge that at least some css is loaded,
        # fonts work so the rest of the static files most likely be loaded too.

        # End of test.

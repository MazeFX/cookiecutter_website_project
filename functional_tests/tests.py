# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: functional/tests.py
Creator: MazeFX
Date: 11-7-2016

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

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class RecruiterVisitTest(LiveServerTestCase):

    def setUp(self):
        caps = DesiredCapabilities.FIREFOX

        # Tell the Python bindings to use Marionette.
        # This will not be necessary in the future,
        # when Selenium will auto-detect what remote end
        # it is talking to.
        caps["marionette"] = True
        self.browser = webdriver.Firefox(capabilities=caps)

    def tearDown(self):
        self.browser.quit()

    def test_browsing_the_recruiter_page(self):

        # Dave has received an job application with all the standard papers but what
        # intrigues is the url link send with the application.
        # Dave fires up a web browser and goes to the url.

        self.browser.get(self.live_server_url)

        # He notices that the page title mentions IT
        self.assertIn('IT', self.browser.title)

        # He sees a page header with a title and particle animation
        header_text = self.browser.find_element_by_id('header-title').text
        self.assertIn('IT', header_text)

        # TODO - Finish user story for functional test
        self.fail('Finish the test!')

    def test_layout_and_styling(self):

        # Dave goes to the recruiter page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

        # TODO - Finish user story for layout test
        self.fail('Finish the test!')

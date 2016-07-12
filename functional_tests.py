# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: functional_tests.py
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

import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class RecruiterVisitTest(unittest.TestCase):

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

        self.browser.get('http://localhost:8000')

        # He notices that the page title and header mention IT
        self.assertIn('IT', self.browser.title)

        # TODO - Finish user story for functional test
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()

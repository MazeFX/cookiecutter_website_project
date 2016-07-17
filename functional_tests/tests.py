# -*- coding: utf-8 -*-

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

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class RecruiterVisitTest(StaticLiveServerTestCase):

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

        # He sees a page header
        header = self.browser.find_element_by_id('recruiter-header')
        # with a title and particle animation
        particles = self.browser.find_element_by_id('particles-js')
        header_text = self.browser.find_element_by_id('header-title').text
        self.assertIn('IT', header_text)

        # He scroll over the page and sees different sections.
        row_top = self.browser.find_element_by_id('row-top')
        row_middle = self.browser.find_element_by_id('row-middle')
        row_bottom = self.browser.find_element_by_id('row-bottom')

        # He sees a link button to send a mail.
        mail_button = self.browser.find_element_by_id('send-mail-button')
        self.assertIn('Mail mij', mail_button.text)

        # He notices a nice footer
        recruiter_footer = self.browser.find_element_by_id('recruiter-footer')

        # Dave is intrigued by the website and wants to send an email
        # by clicking on the mail button
        mail_button.click()

        # Dave is send to a page with an send email form
        self.fail('Finish the test!')

        # Dave enters his credentials and question and click send

        # Dave sees a message that the email has been sent.
        # And another link for going back to the recruiter page.

        # Dave is satisfied with his people skills and congratulates himself
        # with another good person recruited and leaves the page.

        # End of test.

    def test_layout_and_styling(self):

        # Dave goes to the recruiter page
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # He notices the header title has a nice font
        header_title = self.browser.find_element_by_id('header-title-begin')
        header_font = header_title.value_of_css_property('font-family')

        self.assertIn('Droid Sans', header_font)

        # Dave is satisfied with the knowledge that at least some css is loaded
        # so the rest of the static files most likely be loaded too.

        # End of test.

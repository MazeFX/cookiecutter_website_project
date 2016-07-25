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

import sys
import time

from contextlib import contextmanager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of


class RecruiterVisitTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                cls.live_server_url = None
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.live_server_url:
            if cls.server_url == cls.live_server_url:
                super().tearDownClass()

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

    @contextmanager
    def wait_for_page_load(self, timeout=10):
        old_page = self.browser.find_element_by_tag_name('html')
        yield
        WebDriverWait(self.browser, timeout).until(
            staleness_of(old_page)
        )

    def test_browsing_the_recruiter_page_and_sending_an_email(self):

        # Dave has received an job application with all the standard papers but what
        # intrigues is the url link send with the application.
        # Dave fires up a web browser and goes to the url.

        self.browser.get(self.server_url)

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


        with self.wait_for_page_load(timeout=10):
            mail_button.click()

        self.assertIn('Send Email', self.browser.title)

        # time.sleep(5)
        # Dave is send to a page with an send email form

        # He notices the page title and header mention send email

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Send Email', header_text)

        # He is invited to enter his name, email, subject and message.
        inputbox_name = self.browser.find_element_by_id('id_fullname')
        self.assertEqual(
            inputbox_name.get_attribute('placeholder'),
            'Voer je naam in'
        )

        inputbox_name = self.browser.find_element_by_id('id_email')
        self.assertEqual(
            inputbox_name.get_attribute('placeholder'),
            'Voer je email in'
        )

        inputbox_name = self.browser.find_element_by_id('id_subject')
        self.assertEqual(
            inputbox_name.get_attribute('placeholder'),
            'Onderwerp'
        )

        inputbox_name = self.browser.find_element_by_id('id_message')
        self.assertEqual(
            inputbox_name.get_attribute('placeholder'),
            'Bericht'
        )

        # Dave enters his credentials and question
        self.fail('Finish the test!')

        # Dave clicks send

        # Dave sees a message that the email has been sent.
        # And another link for going back to the recruiter page.

        # Dave is satisfied with his people skills and congratulates himself
        # with another good person recruited and leaves the page.

        # End of test.

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

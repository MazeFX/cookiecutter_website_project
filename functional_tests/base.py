# -*- coding: utf-8 -*-

"""
File: functional/base.py
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

from contextlib import contextmanager
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of


class FunctionalTest(StaticLiveServerTestCase):

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


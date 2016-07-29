# -*- coding: utf-8 -*-

"""
File: functional/test_email_validation.py
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
import urllib.parse


class EmailValidationTest(FunctionalTest):

    def test_cannot_input_invalid_values(self):
        # Dave goes to the contact page and is having a very bad day
        # Last night he went and drank way to much so now he is all kinds
        # of mistakes when entering information
        url = urllib.parse.urljoin(self.server_url, '/contact/')
        self.browser.get(url)

        # He at least verifies that it is the correct page
        self.assertIn('Verstuur Email', self.browser.title)

        # Dave doesn't enter anything and submits right away
        # (For testing all fields on empty value validation)
        submit_button = self.browser.find_element_by_id('submit-id-submit')
        with self.wait_for_page_load(timeout=10):
            submit_button.click()

        # He sees that all fields have error messages.
        fullname_error = self.browser.find_element_by_id('error_1_id_fullname').text
        self.assertEqual('Hey je moet wel invullen!', fullname_error)

        email_error = self.browser.find_element_by_id('error_1_id_email').text
        self.assertEqual('Hey je moet wel invullen!', email_error)

        subject_error = self.browser.find_element_by_id('error_1_id_subject').text
        self.assertEqual('Hey je moet wel invullen!', subject_error)

        message_error = self.browser.find_element_by_id('error_1_id_message').text
        self.assertEqual('Hey je moet wel invullen!', message_error)

        # He then enters an invalid email address
        email_input = self.browser.find_element_by_id('id_email')
        email_input.send_keys('Not an email')

        submit_button = self.browser.find_element_by_id('submit-id-submit')
        with self.wait_for_page_load(timeout=10):
            submit_button.click()

        email_error = self.browser.find_element_by_id('error_1_id_email').text
        self.assertEqual('Vul een geldig email adres in.', email_error)

        # He tries again with almost an email address
        email_input = self.browser.find_element_by_id('id_email')
        email_input.clear()
        email_input.send_keys('Almost@email')

        submit_button = self.browser.find_element_by_id('submit-id-submit')
        with self.wait_for_page_load(timeout=10):
            submit_button.click()

        email_error = self.browser.find_element_by_id('error_1_id_email').text
        self.assertEqual('Vul een geldig email adres in.', email_error)

        # Dave enters a correct email address and the email is being sent.
        # Although Dave failed to be a good user the validation check kept
        # him from applying a incomplete or incorrect email.

        # End of test

# -*- coding: utf-8 -*-

"""
File: functional/test_recruiter_visit.py
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

import time
from .base import FunctionalTest


class RecruiterVisitTest(FunctionalTest):

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

        # Dave is send to a page with an send email form
        # He notices the page title and header mention send email
        self.assertIn('Verstuur Email', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Verstuur Email', header_text)

        # He is invited to enter his full name.
        fullname_div = self.browser.find_element_by_id('div_id_fullname')
        self.assertEqual(
            fullname_div.find_element_by_tag_name('label').text,
            'Volledige naam*'
        )
        fullname_div.find_element_by_id('id_fullname').send_keys('Dave Recruiter')

        # He is invited to enter his email address.
        email_div = self.browser.find_element_by_id('div_id_email')
        self.assertEqual(
            email_div.find_element_by_tag_name('label').text,
            'Email adres*'
        )
        email_div.find_element_by_id('id_email').send_keys('Dave@TheITCompany.com')

        # He is invited to enter the email subject.
        subject_div = self.browser.find_element_by_id('div_id_subject')
        self.assertEqual(
            subject_div.find_element_by_tag_name('label').text,
            'Onderwerp*'
        )
        subject_div.find_element_by_id('id_subject').send_keys('(Testmail) I want you to work for us!')

        # He is invited to enter the message text.
        message_div = self.browser.find_element_by_id('div_id_message')
        self.assertEqual(
            message_div.find_element_by_tag_name('label').text,
            'Bericht*'
        )
        message_div.find_element_by_id('id_message').send_keys(
            '''
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
            Vivamus consequat varius justo at viverra. Cras finibus semper
            ligula, vel finibus justo rhoncus a. Nunc non pulvinar urna.
            Vivamus tempus, est quis pulvinar elementum, nulla eros viverra
            leo, eu vestibulum diam mauris et enim. Fusce vitae massa et justo
            vestibulum vestibulum in non sem. Phasellus ipsum nisi, iaculis
            quis imperdiet ut, mollis eu felis. Aliquam maximus nunc vel
            tincidunt maximus. Aliquam at mollis lorem.

            Dear Regards,
            Dave'''
        )

        # Dave pauses for a few seconds to check his message
        time.sleep(3)

        # And then sends the message by clicking submit
        submit_button = self.browser.find_element_by_id('submit-id-submit')
        with self.wait_for_page_load(timeout=10):
            submit_button.click()

        # Dave is sent to a conformation page that the email has been sent.
        self.assertIn('Email Verstuurd', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Email Verstuurd', header_text)

        # And another link for going back to the recruiter page.
        self.fail('Finish the test!')

        # Dave is satisfied with his people skills and congratulates himself
        # with another great developer recruited and leaves the page.

        # End of test.

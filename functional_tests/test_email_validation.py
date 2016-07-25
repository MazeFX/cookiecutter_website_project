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


class EmailValidationTest(FunctionalTest):

    def test_cannot_input_invalid_values(self):
        # Dave goes to the contact page and is having a very bad day
        # Last night he went and drank way to much so now he is all kinds
        # of mistakes when entering information

        # Dave forgets to enter a name
        # TODO - Finish user story

        self.fail('write me!')

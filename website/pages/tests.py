# -*- coding: utf-8 -*-

# GIFS - Clean up the file
# DOCS - Write some documentation

"""
File: tests.py
Creator: MazeFX
Date: 12-7-2016

Tests written for test website pages (home, about, contact, etc)
"""

from django.test import TestCase

class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

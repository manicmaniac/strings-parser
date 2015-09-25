#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from strings.token import *  # noqa


class TestToken(unittest.TestCase):
    def testRepr(self):
        self.assertEqual(repr(Token(EOF)), '<EOF>')
        self.assertEqual(repr(Token(STRING, 'spam')), '<STRING "spam">')

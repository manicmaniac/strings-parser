#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from strings.parser import StringsParser
from strings.token import *  # noqa


class TestStringsParser(unittest.TestCase):
    def setUp(self):
        lexer = MockLexer()
        self.parser = StringsParser(lexer)

    def testParse(self):
        tree = self.parser.parse()
        self.assertEquals(tree.entries[0].key, 'key')
        self.assertEquals(tree.entries[0].value, 'value')


class MockLexer(object):
    def __init__(self):
        self.tokens = iter([Token(LBRACE),
                            Token(STRING, 'key'),
                            Token(EQUAL),
                            Token(STRING, 'value'),
                            Token(SEMICOLON),
                            Token(RBRACE),
                            Token(EOF)])

    def next_token(self):
        return next(self.tokens)

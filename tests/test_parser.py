#!/usr/bin/env python
# -*- coding:utf-8 -*-

import token
import unittest

from strings.parser import StringsParser


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
        self.tokens = iter([(token.LBRACE, None),
                            (token.STRING, 'key'),
                            (token.EQUAL, None),
                            (token.STRING, 'value'),
                            (token.SEMI, None),
                            (token.RBRACE, None),
                            (token.ENDMARKER, None)])

    def get_token(self):
        return next(self.tokens)

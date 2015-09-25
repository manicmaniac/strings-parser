#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from strings.lexer import StringsLexer
from strings.token import *  # noqa


class TestStringsLexer(unittest.TestCase):
    def setUp(self):
        source = '''
        {
            "double quoted key" = "double quoted value";
            'single quoted key' = 'single quoted value';
            raw_key = raw_value;
        }
        '''
        self.lexer = StringsLexer(source)

    def testConsume(self):
        self.assertEqual(self.lexer.char, '\n')
        self.lexer.consume()
        self.assertEqual(self.lexer.char, ' ')

    def testNextToken(self):
        self.assertTokens(Token(LBRACE),
                          Token(STRING, 'double quoted key'),
                          Token(EQUAL),
                          Token(STRING, 'double quoted value'),
                          Token(SEMICOLON),
                          Token(STRING, 'single quoted key'),
                          Token(EQUAL),
                          Token(STRING, 'single quoted value'),
                          Token(SEMICOLON),
                          Token(STRING, 'raw_key'),
                          Token(EQUAL),
                          Token(STRING, 'raw_value'),
                          Token(SEMICOLON),
                          Token(RBRACE),
                          Token(EOF))

    def assertTokens(self, *tokens):
        actuals = []
        expecteds = []
        for expected in tokens:
            actual = self.lexer.next_token()
            actuals.append(actual)
            expecteds.append(expected)
            msg = '->\nactual: {0}\nexpected: {1}'.format(actual, expected)
            self.assertEqual(actual, expected, msg=msg)

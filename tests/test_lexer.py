#!/usr/bin/env python
# -*- coding:utf-8 -*-

import token
import unittest

from strings.lexer import StringsLexer


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

    def testGetToken(self):
        self.assertTokens((token.LBRACE, None),
                          (token.STRING, 'double quoted key'),
                          (token.EQUAL, None),
                          (token.STRING, 'double quoted value'),
                          (token.SEMI, None),
                          (token.STRING, 'single quoted key'),
                          (token.EQUAL, None),
                          (token.STRING, 'single quoted value'),
                          (token.SEMI, None),
                          (token.STRING, 'raw_key'),
                          (token.EQUAL, None),
                          (token.STRING, 'raw_value'),
                          (token.SEMI, None),
                          (token.RBRACE, None),
                          (token.ENDMARKER, None))

    def assertTokens(self, *tokens):
        actuals = []
        expecteds = []
        for expected in tokens:
            actual = self.lexer.get_token()
            actuals.append(actual)
            expecteds.append(expected)
            msg = '->\nactual: {0}\nexpected: {1}'.format(actual, expected)
            self.assertEqual(actual, expected, msg=msg)

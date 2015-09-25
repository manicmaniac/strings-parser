#!/usr/bin/env python
# -*- coding:utf-8 -*-

import collections


token_names = ['EOF', 'LBRACE', 'RBRACE', 'EQUAL', 'SEMICOLON', 'STRING']
__all__ = token_names + ['Token']


EOF = 0
LBRACE = 1
RBRACE = 2
EQUAL = 3
SEMICOLON = 4
STRING = 5


class Token(collections.namedtuple('Token', 'type value')):
    def __new__(cls, type, value=None):
        return super(Token, cls).__new__(cls, type, value)

    def __repr__(self):
        global token_names
        token_name = token_names[self.type]
        if self.value:
            return '<{0} "{1}">'.format(token_name, self.value)
        return '<{0}>'.format(token_name)

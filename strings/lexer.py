#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .token import *  # noqa


class Lexer(object):
    def __init__(self, source):
        self.source = source
        self.pos = 0
        self.char = source[0]

    def consume(self):
        self.pos += 1
        try:
            self.char = self.source[self.pos]
        except IndexError:
            self.char = ''

    def next_token(self):
        raise NotImplementedError()


class StringsLexer(Lexer):
    literals = {'{': LBRACE,
                '}': RBRACE,
                '=': EQUAL,
                ';': SEMICOLON}

    def next_token(self):
        while self.char:
            if self.char.isspace():
                self.whitespace()
            elif self.char in self.literals.keys():
                return self.literal()
            elif self.char in '"\'':
                return self.quoted_string()
            elif self.char.isalnum() or self.char == '_':
                return self.raw_string()
            else:
                raise RuntimeError('unexpected char "{0}"'.format(self.char))
        return Token(EOF)

    def whitespace(self):
        self.consume()

    def literal(self):
        token = Token(self.literals[self.char])
        self.consume()
        return token

    def quoted_string(self):
        quoted_char = self.char
        buf = ''
        self.consume()
        while self.char and self.char != quoted_char:
            buf += self.char
            self.consume()
        self.consume()
        return Token(STRING, buf)

    def raw_string(self):
        buf = ''
        while self.char and self.char.isalnum() or self.char == '_':
            buf += self.char
            self.consume()
        return Token(STRING, buf)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

from strings.token import *  # noqa
from strings.node import StringsNode, EntryNode


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.consume()

    def consume(self):
        self.lookahead = self.lexer.next_token()

    def match(self, type):
        if self.lookahead.type is type:
            value = self.lookahead.value
            self.consume()
            return value
        else:
            raise RuntimeError('expected {0}, {1} found'.format(
                type, self.lookahead))

    def parse(self):
        raise NotImplementedError()


class StringsParser(Parser):
    def parse(self):
        return self.strings()

    def strings(self):
        if self.lookahead.type is LBRACE:
            self.match(LBRACE)
            entries = self.entries()
            self.match(RBRACE)
        else:
            entries = self.entries()
        return StringsNode(entries)

    def entries(self):
        entries = []
        while self.lookahead.type is STRING:
            entries.append(self.entry())
        return entries

    def entry(self):
        key = self.match(STRING)
        self.match(EQUAL)
        value = self.match(STRING)
        self.match(SEMICOLON)
        return EntryNode(key, value)

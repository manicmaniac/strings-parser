#!/usr/bin/env python
# -*- coding:utf-8 -*-

import token

from strings.node import StringsNode, EntryNode


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.consume()

    def consume(self):
        self.lookahead = self.lexer.get_token()

    def match(self, type):
        if self.lookahead[0] is type:
            value = self.lookahead[1]
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
        if self.lookahead[0] is token.LBRACE:
            self.match(token.LBRACE)
            entries = self.entries()
            self.match(token.RBRACE)
        else:
            entries = self.entries()
        return StringsNode(entries)

    def entries(self):
        entries = []
        while self.lookahead[0] is token.STRING:
            entries.append(self.entry())
        return entries

    def entry(self):
        key = self.match(token.STRING)
        self.match(token.EQUAL)
        value = self.match(token.STRING)
        self.match(token.SEMI)
        return EntryNode(key, value)

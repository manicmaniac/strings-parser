#!/usr/bin/env python
# -*- coding:utf-8 -*-

import shlex
import token


class StringsLexer(shlex.shlex):
    literals = {
        '': token.ENDMARKER,
        ';': token.SEMI,
        '=': token.EQUAL,
        '{': token.LBRACE,
        '}': token.RBRACE,
    }

    def __iter__(self):
        return iter(self.get_token, (token.ENDMARKER, None))

    def get_token(self):
        s = shlex.shlex.get_token(self)
        if s in self.literals:
            return (self.literals[s], None)
        if s.startswith(tuple(self.quotes)):
            s = s[1:-1]
        return (token.STRING, s)

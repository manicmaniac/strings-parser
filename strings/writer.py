#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import sys

from ._version import __homepage__ as homepage


class StringsWriter(object):
    default_header = '/* written by strings-parser ({0}) */\n'.format(homepage)
    default_footer = ''

    def __init__(self,
                 file=sys.stdout,
                 header=default_header,
                 footer=default_footer,
                 encoding='utf-32'):
        self.header = header
        self.footer = footer
        self.encoding = encoding
        self.file = codecs.EncodedFile(file, encoding)

    def write(self, strings):
        self.write_header()
        for entry in strings.entries:
            self.write_entry(entry)
        self.write_footer()

    def write_bytes(self, string):
        self.file.write(bytearray(string, self.encoding))

    def write_header(self):
        self.write_bytes(self.header)

    def write_entry(self, entry):
        line = '"{0}" = "{1}";\n'.format(entry.key, entry.value)
        self.write_bytes(line)

    def write_footer(self):
        self.write_bytes(self.footer)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import difflib
import io
import sys
import unittest

from strings.writer import StringsWriter
from strings.node import StringsNode, EntryNode


class TestStringsWriter(unittest.TestCase):
    def setUp(self):
        self.output = io.BytesIO()
        self.encoding = 'utf-8'
        self.writer = StringsWriter(self.output,
                                    header='/* header */\n',
                                    encoding=self.encoding)
        self.node = StringsNode([EntryNode('key1', 'value1'),
                                 EntryNode('key2', 'value2'),
                                 EntryNode('key3', 'value3')])
        self.differ = difflib.Differ()

    def testWrite(self):
        self.writer.write(self.node)
        self.assertOutputEqual('''/* header */
        "key1" = "value1";
        "key2" = "value2";
        "key3" = "value3";
        '''.replace('    ', ''))

    def assertOutputEqual(self, expected):
        actual = self.output.getvalue()
        if sys.version_info >= (3,):
            expected = bytes(expected, self.encoding)
        diff = self.differ.compare(actual.splitlines(), expected.splitlines())
        msg = '\n'.join(diff)
        self.assertEqual(actual, expected, msg=msg)

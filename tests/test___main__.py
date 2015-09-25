#!/usr/bin/env python
# -*- coding:utf-8 -*-

import contextlib
import io
import sys
import unittest

from strings.__main__ import main


class TestMain(unittest.TestCase):
    def setUp(self):
        self.base = 'tests/fixtures/base.strings'
        self.before = 'tests/fixtures/before.strings'
        self.after = 'tests/fixtures/after.strings'

    def testUpdate(self):
        with open(self.after, 'rb') as f:
            expected = f.read()
        with self.capture(main, [self.base, self.before]) as output:
            self.assertEqual(output, expected)

    def testHelp(self):
        with self.capture(main, ['-h']) as output:
            self.assertTrue(output.startswith('A tool to update Localizable'))
        with self.capture(main, ['--help']) as output:
            self.assertTrue(output.startswith('A tool to update Localizable'))

    def testVersion(self):
        with self.capture(main, ['-v']) as output:
            self.assertTrue(output.startswith('0.0'))
        with self.capture(main, ['--version']) as output:
            self.assertTrue(output.startswith('0.0'))

    @contextlib.contextmanager
    def capture(self, callable, *args, **kwargs):
        stdout, sys.stdout = sys.stdout, io.BytesIO()
        callable(*args, **kwargs)
        yield sys.stdout.getvalue()
        sys.stdout = stdout

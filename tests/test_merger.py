#!/usr/bin/env python
# -*- coding:utf-8 -*-


import unittest

from strings.merger import StringsMerger
from strings.node import StringsNode, EntryNode


class TestStringsMerger(unittest.TestCase):
    def setUp(self):
        self.base = StringsNode([EntryNode('spam', 'spam'),
                                 EntryNode('egg', 'egg'),
                                 EntryNode('ham', 'ham')])
        self.localized_before = StringsNode([EntryNode('spam', 'spamspam'),
                                             EntryNode('ham', 'hamham')])
        self.localized_after = StringsNode([EntryNode('spam', 'spamspam'),
                                            EntryNode('ham', 'hamham'),
                                            EntryNode('egg', 'egg')])
        self.merger = StringsMerger(self.base)

    def testUpdate(self):
        merged = self.merger.update(self.localized_before)
        self.assertEqual(merged, self.localized_after)

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from strings.node import Node, StringsNode, EntryNode


class TestNode(unittest.TestCase):
    def setUp(self):
        self.node = Node()
        self.callback_call_count = 0

    def testEq(self):
        self.assertEqual(self.node, Node())

    def testNe(self):
        self.assertNotEqual(self.node, None)

    def testWalk(self):
        self.node.walk(self.callback)
        self.assertEqual(self.callback_call_count, 1)

    def callback(self, node):
        self.callback_call_count += 1


class TestStringsNode(unittest.TestCase):
    def setUp(self):
        entries = [EntryNode('key1', 'value1'),
                   EntryNode('key2', 'value2'),
                   EntryNode('key3', 'value3')]
        self.node = StringsNode(entries)
        self.callback_call_count = 0

    def testEq(self):
        entries = [EntryNode('key1', 'value1'),
                   EntryNode('key2', 'value2'),
                   EntryNode('key3', 'value3')]
        other_node = StringsNode(entries)
        self.assertEqual(self.node, other_node)

    def testNe(self):
        entries = [EntryNode('key1', 'value1'),
                   EntryNode('key3', 'value3'),
                   EntryNode('key2', 'value2')]
        other_node = StringsNode(entries)
        self.assertNotEqual(self.node, other_node)

    def testWalk(self):
        self.node.walk(self.callback)
        self.assertEqual(self.callback_call_count, 4)

    def callback(self, node):
        self.callback_call_count += 1


class TestEntryNode(unittest.TestCase):
    def setUp(self):
        self.node = EntryNode('key', 'value')
        self.callback_call_count = 0

    def testEq(self):
        self.assertEqual(self.node, EntryNode('key', 'value'))

    def testNe(self):
        self.assertNotEqual(self.node, EntryNode('k', 'v'))

    def testWalk(self):
        self.node.walk(self.callback)
        self.assertEqual(self.callback_call_count, 1)

    def callback(self, node):
        self.callback_call_count += 1

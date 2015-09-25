#!/usr/bin/env python
# -*- coding:utf-8 -*-


from itertools import starmap
from operator import eq


class Node(object):
    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __ne__(self, other):
        return not self.__eq__(other)

    def walk(self, func):
        func(self)


class StringsNode(Node):
    def __init__(self, entries):
        self.entries = entries or []

    def __eq__(self, other):
        if all(starmap(eq, zip(self.entries, other.entries))):
            return super(StringsNode, self).__eq__(other)
        return False

    def walk(self, func):
        for entry in self.entries:
            func(entry)
        super(StringsNode, self).walk(func)


class EntryNode(Node):
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __eq__(self, other):
        if self.key == other.key and self.value == other.value:
            return super(EntryNode, self).__eq__(other)
        return False

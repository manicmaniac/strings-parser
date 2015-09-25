#!/usr/bin/env python
# -*- coding:utf-8 -*-

import copy
import difflib

from .node import StringsNode, EntryNode


class StringsMerger(object):
    def __init__(self, base):
        self.base = base
        self.matcher = difflib.SequenceMatcher()
        base_keys = self.extract_keys(base)
        self.matcher.set_seq2(base_keys)

    def update(self, localized):
        merged_entries = []
        for tag, i1, i2, j1, j2 in self.opcodes_for_keys(localized):
            if tag in ('replace', 'insert'):
                entries = copy.copy(self.base.entries[i1:i2])
                merged_entries += entries
            elif tag == 'delete':
                pass
            elif tag == 'equal':
                entries = zip(self.base.entries[i1:i2],
                              localized.entries[j1:j2])
                for base_entry, localized_entry in entries:
                    merged_entry = EntryNode(base_entry.key,
                                             localized_entry.value)
                    merged_entries.append(merged_entry)
        return StringsNode(merged_entries)

    def opcodes_for_keys(self, localized):
        localized_keys = self.extract_keys(localized)
        self.matcher.set_seq1(localized_keys)
        for tag, i1, i2, j1, j2 in self.matcher.get_opcodes():
            yield (tag, i1, i2, j1, j2)

    def extract_keys(self, strings):
        return [entry.key for entry in strings.entries]

#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""A tool to update Localizable.strings

Usage:
    python -m strings (-h | --help)
    python -m strings (-v | --version)
    python -m strings <base.strings> <localizable.strings>

Options:
    -h --help     show this screen
    -v --version  show version string
"""

import getopt
from os.path import abspath, basename, dirname
import sys

cwd = dirname(abspath(__file__))

sys.path.insert(0, dirname(cwd))
from strings._version import __version__
from strings.lexer import StringsLexer
from strings.parser import StringsParser
from strings.merger import StringsMerger
from strings.writer import StringsWriter
sys.path.pop(0)


def make_ast(path):
    with open(path, 'rb') as f:
        source = f.read()
    lexer = StringsLexer(source)
    parser = StringsParser(lexer)
    return parser.parse()


def update(base, localizable):
    base_ast = make_ast(base)
    merger = StringsMerger(make_ast(base))
    updated = merger.update(make_ast(localizable))
    writer = StringsWriter(file=sys.stdout, encoding='utf-8')
    writer.write(updated)


def main(args=sys.argv[1:]):
    try:
        options, args = getopt.gnu_getopt(args, 'hv', ['help', 'version'])
    except getopt.GetoptError as e:
        sys.stderr.write('error: {0}\n'.format(e))
        return 2
    if ('-h', '') in options or ('--help', '') in options:
        sys.stdout.write(__doc__ + '\n')
        return 1
    if ('-v', '') in options or ('--version', '') in options:
        sys.stdout.write(__version__ + '\n')
        return 1
    argc = len(args)
    if argc != 2:
        message = 'error: wrong number of arguments ({0} for 2)\n'.format(argc)
        sys.stderr.write(message)
        return 2
    update(args[0], args[1])


if __name__ == '__main__':
    sys.exit(main())

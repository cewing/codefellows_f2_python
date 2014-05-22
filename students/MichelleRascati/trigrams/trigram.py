#!/usr/bin/env python
import codecs


def trigram(in_file):
    orig = codecs.open(in_file)
    orig_lines = map(str.strip, orig.readlines())
    print orig_lines

#!/usr/bin/env python
"""
Generators
"""


def intsum():
    i = 0
    n = 0
    while True:
        yield i
        n += 1
        i = i + n


def intsum2():
    i = 0
    n = 0
    while True:
        yield i
        n += 1
        i = i + n

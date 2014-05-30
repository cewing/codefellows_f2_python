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


def doubler():
    i = 1
    while True:
        yield i
        i = i * 2


def fib():
    i = 1
    last = 0
    while True:
        yield i
        i = i + last
        last = i - last

#!/usr/bin/python
# -*- coding: utf-8 -*-

from __init__ import unique


strings = [
    ('', ('', {})),
    ('a', ('a', {'a': 1})),
    ('aa', ('a', {'a': 1})),
    ('ab', ('ab', {'ab': 2})),
    ('aba', ('ab', {'ab': 2, 'ba': 2})),
    ('abbcdeee', ('bcde', {'ab': 2, 'bcde': 4, 'e': 1})),
    ('xabcdaefghg', ('bcdaefgh', {'xabcd': 5, 'bcdaefgh': 8, 'hg': 2})),
    ('nnnghiusgxxfghgg', ('nghius', {'n': 1, 'nghius': 6, 'hiusgx': 6, 'xfgh': 4, 'hg': 2, 'g': 1})),
    ('fghg', ('fgh', {'fgh': 3, 'hg': 2})),
    ('ghg', ('gh', {'gh': 2, 'hg': 2})),
]


if __name__ == '__main__':

    # Проверка работы исключений
    try:
        r = unique(123)
        print("\n", "Exceptive function call returned %s" % (r,), sep='')
        print("Exception check Failed", "\n")
    except ValueError as e:
        print("\n", e, sep='')
        print("Exception check OK")

    # Проверка обработки входных данных
    for i, s in enumerate(strings):
        try:
            test = unique(s[0])
            assert test == s[1]
            status, error = 1, ''
        except AssertionError:
            status, error = 0, "\n%s != %s\n" % (test, s[1])
        print("Test %s: %s -- %s%s" % (i, s[0], ["Failed", "OK"][status], error))

    print()

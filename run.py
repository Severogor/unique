#!/usr/bin/python
# -*- coding: utf-8 -*-

from __init__ import unique


if __name__ == '__main__':

    s = input("\nInput: ")
    i = True
    while s or i:
        c, a = unique(s)
        print("Substring:", c)
        print("Contents:", a)
        if not s:
            i = False
        s = input("\nInput: ")

    print()
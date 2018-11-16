#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) Severogor
# 16.11.2018


def unique(string: str) -> tuple:
    """
      Split string into substrings consisting of only unique symbols
        string :  input string

      returns :  (longest substring, {substring: length, ...})
    """

    if type(string) is not str:
        raise ValueError("Expected object of type str, but an object of type %s was given" % (type(string).__name__,))

    # Подстрока
    chunk = ''
    # Итоговый набор
    chunks = {}
    # Символьная таблица с индексами
    symbols = {}
    # Рабочая подстрока
    sub = ''
    # Смещение
    start = 0
    # Пока не достигнут конец строки
    while start < len(string):
        i = start
        s = string[i]
        # Пока есть следующий символ и он уникален
        while s and s not in symbols:
            sub += s
            symbols[s] = i
            s = string[i+1:i+2]
            i += 1

        # Запись и сравнение полученной подстроки
        chunks[sub] = len(sub)
        if chunks[sub] > len(chunk):
            chunk = sub

        # Отбрасывание "хвоста" до повторяющегося символа
        if i < len(string):
            start = symbols[string[i]]
        # Чтобы не брать подмножества
        else:
            break

        # Начало обработки следующей подстроки
        symbols = {}
        sub = ''
        start += 1

    return chunk, chunks


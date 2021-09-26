#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = str(input('Введите что-либо: ')).lower()
    b = str(input('Введите что-либо второй раз: ')).lower()
    c = set(a) & set(b)
    print(c)

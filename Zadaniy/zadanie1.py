#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    a = str(input('Введите слово: ')).lower()
    b = 0
    c = set("аоэеиыуёюя")
    for i in a:
        if i in c:
            b += 1
    print(f"Количество гласных букв в слове {a}: {b}")




#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"b", "e", "g", "h", "k", "s"}
    b = {"c", "g", "p", "q"}
    c = {"f", "g", "s", "x", "y", "z"}
    d = {"a", "c", "d", "g", "u", "v", "z"}

    x = (a.union(b)).intersection(c)
    print(f"x = {x}")

    # Найдем дополнения множеств
    an = u.difference(a)

    y = (an.intersection(d)).union(c.difference(b))
    print(f"y = {y}")
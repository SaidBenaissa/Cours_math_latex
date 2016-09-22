#!/usr/bin/env python3

from random import random

m = 0
for i in range(1000):
    n = 0
    for j in range(5696):
        if random() < 0.00052:
            n = n + 1
    if n >= 9:
        m = m + 1
print(m)

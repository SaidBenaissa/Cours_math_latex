from random import randint
from math import sqrt

simulations = 10000
n = 40

fluc_min = 15.0/36 - 1/sqrt(n)
fluc_max = 15.0/36 + 1/sqrt(n)

dedans = 0.0

for i in range(simulations):
    somme = 0.0
    for i in range(n):
        if randint(1,6) + randint(1,6) >= 8:
            somme += 1
    if somme/n > fluc_min and somme/n < fluc_max:
        dedans += 1

print(dedans / simulations)

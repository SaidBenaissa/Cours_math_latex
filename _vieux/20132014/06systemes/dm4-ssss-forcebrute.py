#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def forcebrute(points):
    """Cassage par force brute du code utilisant SSSS avec les arguments.

    Entrée : Une liste de points du plan.
    Sortie : La liste des couples (a, b), où a et b sont des chiffres
        (entiers entre 0 et 9), tels que tous les points donnés en argument
        font partie de la courbe représentative du polynôme x->ax+b.
    """
    solutions = []
    for a in range(0, 10):
        for b in range(0, 10):
            if all([a*x + b == y for (x, y) in points]):
                solutions.append((a, b))
    return solutions

if __name__ == "__main__":
    print("Cassage de (3, 15)...")
    print(forcebrute([(3, 15)]))

    #print("Cassage de (-1, 4), (0.5, 5.5)...")
    #print(forcebrute([(-1, 4), (0.5, 5.5)]))

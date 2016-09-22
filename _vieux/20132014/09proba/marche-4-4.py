#!/usr/bin/env python3

import random
from turtle import *

################################################################################
# Initialisation du programme.
################################################################################
hauteur=10
largeur=10
est=largeur/2
ouest=-est
nord=hauteur/2
sud=-nord


def restart():
    reset()
    setworldcoordinates(-20, -20, 20, 20)

    home()
    color("red")
    width(2)
    up()
    goto(ouest,nord)
    down()
    goto(est,nord)
    goto(est,sud)
    goto(ouest,sud)
    goto(ouest,nord)
    up()
    home()
    down()
    width(8)
    color("green")

################################################################################
# Ne modifiez pas au lignes au dessus de celle-ci à moins que l'énoncé vous le dise.
# Vous pouvez modifier les lignes en dessous.
################################################################################

restart()
tracer(100, 0)

somme = 0
for i in range(100):
    pas = 0
    restart()
    while abs(xcor())<5 and abs(ycor())<5:
        r = random.randint(1,4)
        if r == 1:
            left(90)
        elif r == 2:
            right(90)
        elif r == 3:
            left(180)
        forward(1)
        pas = pas + 1
    somme = somme + pas
    print(pas)
print("Moyenne", somme/100)

mainloop()

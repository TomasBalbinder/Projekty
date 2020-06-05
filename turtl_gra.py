'''
zelvi grafika, vykresli vetrnik 
od uzivatele nacte vstup na pocet lopatek
'''

from turtle import left , forward , exitonclick
import math


def lopatka():
    forward(100)
    left(180 - 45)
    forward(math.sqrt(50**2 + 50**2))
    left(90)
    forward(math.sqrt(50**2 + 50**2))
    left(180 - 45)

def vetrnik(uzivatel):
    for i in range(uzivatel):
        lopatka()
        left(360 / uzivatel)
    exitonclick()

uzivatel = int(input("Zadej pocet lopatek: "))
vetrnik(uzivatel)
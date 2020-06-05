# pokracovani ve vytvareni jednoduchych programech

"""
Vytvor program ktery rozdely 
ruzny pocet jablek a deti ktery zvoli uzivatel sam.

1. vstup od uzivatele - zada pocet deti a jablek
2. vypocet bez zbytku
3. vysledek 
"""

jablka = int(input("Zadej pocet jablek: "))
deti = int(input("Zadej pocet deti: "))
# komplexnejsi zapis
vypocet, zbytek = jablka // deti, jablka % deti


print("Na jedno dite vychazi {} jablek.".format(vypocet))
print("Zutane mi {} jablek.".format(zbytek))


'''
Vytvor program ktery vypise z kolika jednotek,
desitek, stovek a tisicu se sklada cislo na vstupu

1. vstup od uzivatele (prirozene cislo)
2. vypocet (rozdeleni cislenych hodnot.)
3. vystup v podobe rozdeleni

'''

cislo = int(input("Zadej cislo: "))
# vypocet tisicu
tisic = cislo
tisic = tisic // 1000
zbytek = cislo % 1000

# vypocet stovek
sto = zbytek // 100
zbytek = zbytek % 100

# vypocet desitek
deset = zbytek // 10
zbytek = zbytek % 10

# vypocet jednotek
jedna = zbytek // 1

print("Cislo {} obsahuje {} * 1000, {} * 100, {} * 10 a {} * 1. ".format(cislo,tisic,sto,deset,jedna))

'''
Vytvor program ktery rozdeli castku na mince nominalni hodnoty
50, 20, 10, 5, 2, 1.

1. vstup od uzivatele (cele cislo)
2. vypocet - vyuzijeme deleni bezezbytku
3. vystup v podobe roztridenych minci

'''

hodnota = int(input("Zadej castku na rozdeleni: "))

padesat = hodnota          
padesat = padesat // 50    
zbytek = hodnota  % 50

dvacet = zbytek // 20
zbytek = zbytek  % 20

deset = zbytek // 10
zbytek = zbytek  % 10

pet = zbytek // 5
zbytek = zbytek  % 5

dva = zbytek // 2
zbytek = zbytek  % 2

jedna = zbytek // 1

print("50 *", padesat)
print("20 *", dvacet)
print("10 *", deset)
print("5 *", pet)
print("2 *", dva)
print("1 *", jedna)

'''
Vytvor program ktery rozdeli desetine cislo 
na celou a desetinou cast.

1. vstup od uzivatele v podobe float 
2. vypocet - import modulu math metoda modf, tuple - zmena poradi,
zmena datoveho typu na str - zaokruhleni.
3. vystup 
'''
import math
vstup = float(input("Zadej cislo: "))

rozdeleni = math.modf(vstup)[::-1]

for rozdel in rozdeleni:
    prevod = str(rozdel)
    print(prevod[:5])


'''
Vypocet uhlu sinus a cosinus ve stupnich
ktere si sam zada uzivatel

Pouzijeme modul math s metodou sin a cos
1. vstup od uzivatele
2. vypocet 
3. vystup 

'''

from math import sin, cos, radians, pi

uhel = float(input("Zadej uhel ve stupnich: "))

uhelRadiany = radians(uhel)
print("Sinus", sin(uhelRadiany))
print("Cosinus", cos(uhelRadiany))



'''
Samostatny algoritmus na vypocet faktorialu vlozeneho cisla

1. nacteni vstupu (hodnoty)
2. vypocet
3. vystup

'''
import math

cislo = int(input("Zadej cele kladne cislo: "))

if cislo > 0: 
    faktorial = math.factorial(cislo)
    print("Faktorial cisla {} je {} faktorial".format(cislo,faktorial))
else:
    print("Musis zadat kladne cislo.")

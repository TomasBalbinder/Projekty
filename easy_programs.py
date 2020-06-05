"""
Jednoduche programy v prikazove radce

vstup: jmeno, prijmeni
vystup: pozdrav vcetne jmena

1. nacteni vstupu od uzivatele
2. zpracovani dat
3. vypsani dat od uzivatele 
"""

jmeno = input("Zadej sve jmeno: ")
prijmeni = input("Zadej sve prijmeni: ")

cele_jmeno = jmeno + " " + prijmeni
pozdrav = "Ahoj " + cele_jmeno

print(pozdrav)


"""
jednoduchy program na vypocet 
obsahu a obvodu ctverce

1. vstup od uzivatele
2. vypocet - vzorec pro obvod a obsah ctverce
3. vyledek
"""

strana_a = input("Zadej delku strany: ")
strana_a = float(strana_a)

print("Obvod ctverce:", 4 * strana_a ,"\nObsah ctverce:", strana_a ** 2)


"""
program pro vypocet obdelniku: obvodu a obsahu.
Delky stran obdelniku si zada uzivatel sam. 

1. vstup od uzivatele
2. vypocet 
3. vystup 
"""
strana_a = float(input("Zadej delku strany A: "))
strana_b = float(input("Zadej delku strany B: "))

print("Obvod: ", 2 * (strana_a+strana_b), "\tObsah: ", strana_a * strana_b)

"""
Vytvor program pro vypocet obvodu a obsahu kruhu.
Delku polomeru zada uzivatel

1. vstup od uzivatele
2. vypocet
3. vystup 
"""

polomer = float(input("Zadej delku polomeru: "))

o = 2 * 3.14 * polomer
S = 3.14 * polomer ** 2

print("Obvod:", round(o), "\nOBsah:",  round(S))
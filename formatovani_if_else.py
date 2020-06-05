

"""
Vyzkouseni ruznych moznosti formatovani s hodnotou pi.
V  ciklu vypisu 0 az 10 mocninu cisla 10 formatove 
zarovnanou vpravo.
"""
# pozustatek od jazyka C
# f - float, prvni cislice znaci celkovy pocet policek, druha od tecky dozadu.
import math
print("%10.4f"%(math.pi))

# funkce pow vytvari mocninu
# 0 pred cislem 20 znamena ze se volne pozice pred cislem zaplni nulou.
for mocnina in range(11):
    print("%20.i"%(pow(10,mocnina)))

'''
V cyklu vypis 0 az 15 hodnotu hexadecimalni ciselne soutavy.
Bude se jedna o cisla 0-9  a pimena A-F, odsazenost 4bity.
'''

for cislo in range(16):
    print("%X"%(cislo),end= " ")


'''
Vyzkouseni runych moznosti formatovani s prefixem f 
a metodou format pro text, desetine a cele cislo.

'''
import math

pi = math.pi
text = "Ahoj"
cislo = 12345
# prvni cislo znaci poradi formatu, pak nasleduje dvojtecka a cisla zobrazujici odsazeni.
print("\n%.20f"%(pi))
print("\n{2:} {1:10.3} {0:.4}".format(pi,text,cislo))
print(f"{pi:.3f}, {text}") # promene se rovnou zapisuji do zavorek, musi obsahovat prefix f
# ruzne formatovani ">" zarovnani doprava, "<" zarovnani doleva, "0" predrazena nula
for i in range(1,12):
    print(f"{i:>20}")


for cislo in range(1,11):
    moc = pow(10,cislo)
    print(f"{cislo:2}: {moc:<15}")

'''
Vytvor program ktery vypise 0 az 10 mocninu vlozeneho
jednociferneho prirozeneho cisla 1 az 9. Prozatim neosetruj 
podminkou. Formatovani nekterym z python zpusobu tnz f nebo format.
Zarovnane doprava s predrazenymi nulami. 
'''

mocniny = int(input("Zadej cislo 1 az 9: "))
if mocniny in range(1,10):
    for mocnina in range(11):
        vypocet =pow(mocniny,mocnina)
        print(f"{mocnina:>2}: {vypocet:>010}")
else:
    print("Zadej mensi cislo. Mezi 1 az 9!")


'''
Vytvor program pro vypis faktorialu
vlozeneho prirozeneho cisla.
Vstup osetri podminkou. 
'''

import math

cislo = int(input("Zadej prirozene cislo: "))

if cislo > 0:
    faktorial = math.factorial(cislo)
    print(f"{cislo:>5} = {faktorial:>5}")

else:
    print("Nebylo zadano prirozene cislo.")


'''
Vytvor program ktery nacte uzivatelovu odpoved
(pouze 0=ne ci 1=ano)

'''

odpoved = int(input("Ucis se python? Zadej 0 ci 1: "))

if odpoved in range(0,2):
    odpoved = bool(odpoved)    
    if odpoved:
        print("Ano mas pravdu.")

    else:
        print("Ne, lzes!")
else:
    print("Nezadal jsi ani 0 ani 1")


'''
Vytvor program kterz nacte vlozene 
cislo a dle volby uzivatele vypise:
druhou mocninu (volba1), druhou odmocninu (volba2),
faktorial (volba3).
'''

import math

print('''Zvol z moznosti: volba 1 - vypise druhou mocninu\n                 volba 2 - vypise druhou odmocninu\n                 volba 3 - vypise faktorial''')
volba = int(input("Zadej cislo: "))

if volba == 1:
    mocnina =int(input("Zadej cislo pro vypocet mocniny: "))
    print(f"Mocnina cisla {mocnina} =",pow(mocnina,2))

elif volba == 2:
    odmocnina =int(input("Zadej cislo pro vypocet odmocniny: "))
    print(f"Odmocnina cisla {odmocnina} =",math.sqrt(odmocnina))

elif volba == 3:
    faktorial =int(input("Zadej cislo pro vypocet faktorialu: "))
    print(f"Faktorial cisla {faktorial} =",math.factorial(faktorial)) 
else:
    print("Zadal jsi spatne cislo, zkus to znovu.")

'''
Vytvor program ktery dle zadaneho
cisla vyhodnoti zda li je sude ci liche.

vstup: cislo
vystup: suda/licha
'''

cislo = int(input("Zadej cislo: "))
sude = cislo % 2
if sude == 0:
    print("mas sude")
else:
    print("mas liche")
    



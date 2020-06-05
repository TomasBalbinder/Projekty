'''
Vygeneruj nahodny petimisty captcha kod
slozeny ze znaku a-z, A-Z, 0-9 a uloz je 
do seznamu. V cyklu captcha kody vypisuj 
na monitor a po uzivateli vyzaduj aby je
prepisoval.
Pocitej uspesnost opisu.
'''

import random

abc = """abcdefghijklmnopqrstuvwxyz0123456789
ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
seznam = []
opis = 1
kontrola = []
for i in range(0,5):    
    vyber = random.choice(abc)
    seznam.append(vyber)
string = ''.join(seznam)
print(string)
uzivatel = input("Zadej captcha kod pro overeni: ")

while uzivatel != string:
    kontrola.append(uzivatel==string)    
    opis += 1
    print(string)
    uzivatel = input("Zadej captcha kod pro overeni: ")         
print("Zadal jsi spravny kod.")
print(f"{opis}x jsi zadal heslo z toho {len(kontrola)}x spatne.")



'''
Vytvor hru pro trening mozku.
Poznas co znamena slovo ci 
CREEVN? Lidskemu mozku staci znat prvni
a posledni pismeno ostatni pismena mohou 
byt prehazena a presto text dokazes precist.
'''
import random

slovo = input("Zadej slovo: ")
pocitadlo = len(slovo)

seznam = []
prostedek = []
for i in slovo:
    seznam.append(i)
for j in seznam[1:-1]:
    prostedek.append(j)

random.shuffle(prostedek)
prostedek = "".join(prostedek)
seznam = "".join(seznam)
spojeni = seznam[0] + prostedek + seznam[pocitadlo - 1]
#print(f'Slovo pred zamichanim: {slovo}')     
print(f"Slovo po zamichani: {spojeni}")

hadani = input("Hadej slovo: ")
while slovo != hadani:   
    print("Spatne, zkus to znovu.")
    hadani = input("Hadej slovo: ")
print("Spravne, uhadl jsi!")



# Sifrovani textu

retezec = input("Zadej: ")
znaky = "ABEGHIOSTZ"
leet = "4836410572"

retezec = list(retezec.upper())


for i in range(0,len(retezec)):
    pismena = retezec[i]
    if pismena in znaky:
        index = znaky.find(pismena)
        retezec[i]= leet[index]
print("-".join(retezec))




'''
Prevod z desitkove na 
dvojkovou soustavu
'''

cislo = int(input("Zadej cislo: "))

seznam = list()
x = cislo
while x > 0:
    zbytek = x % 2
    seznam.append(zbytek)
    x = x // 2

zacatek = len(seznam) -1
konec = -1 
krok = -1

for i in range(zacatek, konec, krok):
    print(seznam[i],end="")


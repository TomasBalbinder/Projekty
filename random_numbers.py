
'''
Vytvor program ve kterem si 
vyzkousis nektere funkce knihovny
random. Program zkombinuj
s cykly a seznamy.
Napr: generovani cisla
      vyber nahodneho znaku, prvku z retezce, seznamu
      promichani polozek seznamu
      generovani nahodnych polozek seznamu
'''
import random

# generovani cisla 
for i in range(0,5):
    cislo = random.random()
    print(cislo)

seznam = []   
for i in range(1,10):
    # nahodne vytvori seznam cisel od 1 do 10.
    seznam.append(random.randint(1,10))
print(seznam)
# nahodne vybere cislo ze seznamu  
print(f"{random.choice(seznam)}")  
print("------------------------------------")
seznam = []   
i = 0

while i < 10:
    cislo = random.randint(1,10)
    if cislo not in seznam:
        seznam.append(cislo)
        i = i + 1
seznam.sort()
for i in seznam:
    print(f"{i}")

random.shuffle(seznam) # nahodne rozhazi serazena cisla
for i in seznam:
    print(f"{i}")    


s = "ABCEDEFGE"
print(random.choice(s), s)

k = list(s)
print(k)
random.shuffle(k) # shuffle pouze jako seznam
print(k)

seznam = list()
x = int(input("Zadej pocet polozek seznamu: "))

for i in range(0,x):
    seznam.append(random.randint(1,10))

print(seznam)



'''
Vytvor program ktery vygeneruje 
x unikatnich nahodnych cisel v rozahu od 
1 - 80. Cisla ukladej do seznamu.
'''

import random
seznam = list()

for i in range(1,81):
    cislo = random.randint(1,80)
    if cislo not in seznam:
        seznam.append(cislo)
seznam.sort()
print(f"{seznam}")



'''
Vytvor program ktery vygeneruje tabulku 
o poctu radku a sloupcu "a" x "b" naplnenou 
nahodnymi znaky A-Z.
'''
import random
abc = "ABCDEFGHIJKLMNOPQRTUVWXYZ"

a = int(input("Zadej pocet radku: "))
b = int(input("Zadej pocet sloupcu: "))
if a > 0 and b > 0:
    for i in range(0,a):
        for j in range(0,b):
            print(random.choice(abc),end=" ")
        print()

# Samozrejme dalo by se doplnit o else
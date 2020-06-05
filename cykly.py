 
zacatek = int(input("Zadej zacatek cyklu: "))
konec = int(input("Zadej konec cyklu: "))
vypocet = 0
licha = 0
if zacatek < konec:           
    for i in range(zacatek, konec + 1):
        print(i)
        vypocet += i
        if i % 2 != 0:
            licha += 1
    print(f"Prumer je {vypocet} / {konec - zacatek +1} = {vypocet / (konec - zacatek +1)}")       
    print(".......................")
    print(f"Pocet lichych cisel je/jsou {licha}")
    print(f"Pocet sudych cisel je/jsou {konec - zacatek +1 - licha}")
        
    print(".......................")
    i  = zacatek
    while i <= konec:
        print(i)
        i = i + 1
else:
    print("Zadana spatna cisla")



'''
Vypis na monitor ctverec
z hvezdicek. Delku strany ctverce 
zada uzivatel na vstupu.
'''

hvezdicky = int(input("Zadej delku strany ctverce: "))

if hvezdicky > 0:
    for i in range(hvezdicky):
        print("* " * hvezdicky)

    print()
    i = 0
    while i < hvezdicky:
        print("* " * hvezdicky)
        i = i + 1
else:
    print("Zadej kladna cisla")



'''
Vypis na monitor malou nasobilku cisel 1 -10.
Nasobilku formatuj do vzhledove tabulky.
'''

for i in range(1,11):
    for j in range(1,11):
        print(f"{i * j:>5}", end="")
    print()



'''
Vytvor progrm pro postupne nacitani  cisel
a vyhodnot jejich soucet, minimum a maximum.
Radu cisel ukonci cislici 0.
'''

cislo = int(input("Zadej cislo: "))
suma = 0 
prumer = 0 
while cislo != 0:
    prumer = prumer + 1 
    suma = suma + cislo
    if prumer == 1:
        min = cislo 
        max = cislo 
    else:
        if cislo < min:
            min = cislo
        elif cislo > max:
            max = cislo
    cislo = int(input("Zadej cislo: "))
print("Soucet cisel je", suma,"Maximum:", min, "Minimum:", max)
   

'''
Vytvor program pro postupne zadavani znamek
celych cisel v rozsahu od 1 - 5. Pokud uzivatel 
zada cislo mimo rozsah cyklus bude ukoncen.
Vypis kolik znamek uzivatel zadal.
'''


cislo = int(input("Zadej 1. znamku od 1 - 5: "))
prumer = 0
while cislo < 6 and cislo > 0: # da e resit pres in range(1,6)
   
    prumer = prumer + 1
    cislo = int(input(f"Zadej {prumer + 1} znamku od 1 - 5: "))

print(f"Bylo zadano {prumer} znamek.")

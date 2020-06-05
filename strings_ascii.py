



"""
Uloz do promenne retezec, zjisti jeho delku,
vypis jeho prvni a posledni znak.
"""
import time
retezec = "bublifuk"
delka = len(retezec)
print(f"Delka retezce {delka} a prvni a posledni pismeno {retezec[0]} a {retezec[delka - 1]}")

for i in range(0, delka):
    print(retezec[i])
    time.sleep(1/10)

chr() # do zavorek zadame cislo od 0 do 256 podle ASCII tabulky
ord() # do zavorek zadame znak a vystup bude cislo z ASCII tabulky

'''
Vypis tabulku ASCII
'''
for i in range(0,256):    
    print(f"{i}: {chr(i)}\t", end=" ")

'''
Do jedne promenne nacti cele 
jmeno osoby. Vypis inicialy osoby.
Vypis jmneo a prijmeni malymi pismeny.
Velkymi pismeny, vyzkousej ruzne kombinace.
'''

promena = "Tomas Novotny Pes"
jmeno, prijmeni, pes = promena.split()
print(f"{jmeno[0]} {prijmeni[0]} {pes}")

print(promena.lower())
print(promena.upper())

'''
Nacti vek uzivatele jako retezec.
Kdyz bude obsahovat cislice,
preved jej na cele cislo jinak vypis 
chybovou hlasku.
Veku vypis na monitor spolu  datovym typem.
'''

vek = input("Zadej vek: ")

if vek.isdigit():
    vek = int(vek)      
    print(type(vek),f"{vek}")
else:
    print("Mas chybu v zapisu")


kde = "jahoda"
print(kde.ljust(50))
print(kde.center(50))


kluci = "Eva", "Linda", "Jana", "Eva"
print(kluci)

"""
Napis program ktery vypise nabidku kavarny,
tedy nazev napoje, jeho objem a cenu.
Vystup formatuj do prehledne tabulky.
Data budou ve sloupcich.
"""

print("Nabidka Kavarny".center(30))

napoje = "kola", "kava", "dzus", "mineralka", "pivo"
objem = "0.3", "0,2", "0.5", "0.5", "0.5"
cena = "33", "45", "25", "15", "21"
nap = len(napoje)
for i in range(nap):
    print(f"{napoje[i].ljust(10)} {objem[i]:>5} dl {cena[i]:>5} Kc")



'''
Napis program ktery nacte nazvy 
komodit ktere uzivatel nakoupil.
Dale nacte mnozstvi ktere za kazdou
komoditu nakoupil.
Nakonec do prehledne tabulky vypise ucet, napr:
'''

komodity = input("Zadej zbozi: "), input("Zadej zbozi: "), input("Zadej zbozi: ")
mnozstvi = int(input("Zadej mnozstvi: ")), int(input("Zadej mnozstvi: ")), int(input("Zadej mnozstvi: ")),
cena = 15, 25, 3, 30

poctadlo= len(komodity)
for i in range(poctadlo):
    print(f"{komodity[i].ljust(7)}{mnozstvi[i]:>5} * {cena[i]} = {cena[i] * mnozstvi[i]:>4}")






'''
cislo = input('Zadej cislo: ')
elementy = ' + '.join(f'{nasobek} * 1{(len(cislo) - mocnina - 1) * "0"}'for mocnina, nasobek in enumerate(str(cislo)))
print(f'{cislo} = ' + elementy)
'''



'''
Nacti retezec obsahujici cifry a znaky.
Retezec prochazej znak po znaku a znaky
rozdeluj do skupin: pismena, cifry,
jine znaky. Vypis kolik znaku kazda skupina obahuje.
'''

retezec = "asdasdADDDWAD08464\\-//+*"
delka = len(retezec)
pocet_cisla = 0
pocet_pismen = 0
pocet_cifer = 0
for i in range(delka):
    if retezec[i].isdigit():
        pocet_cisla = pocet_cisla + 1
    if retezec[i].isalpha():
        pocet_pismen = pocet_pismen + 1
    if retezec[i].isascii():
        pocet_cifer = pocet_cifer + 1

print(f"Pocet cisel: {pocet_cisla}\nPocet pismen: {pocet_pismen}\nPocet cifer: {pocet_cifer}")

znak = input("Zadej znak: ")

if znak in retezec:
    print("Znak uz tam je")

else:
    print("Znak tam jeste neni")


'''
Vytvor priklad ktery roztridi 
vsechny znaky 7 bitove ACSCII
tabulky na pismena, cifry a jine znaky.
Jednotlive skupiny ukladej do novych promennych
nakoenc vypis jejich obsah a pocet za kazdou 
skupinou. 
'''
cisla = ""
slova = ""
cifra = ""

for i in range(0,128):    
    znaky = chr(i)
    if znaky.isdigit():
        cisla += znaky       
    else:
        if znaky.isalpha():
            slova += znaky           
        else:
            if znaky.isascii():
                cifra += znaky
print(f"Cisla: {cisla} = {len(cisla)}")
print(f"Pismena: {slova} = {len(slova)}")
print(f"Cifry: {cifra} = {len(cifra)}")



'''
Uzivatel zada cele cislo.
Program bude vyhodnocovat, 
zdali se jedna nejedna o skolni
znamku (tnz. o cislo v rozsahu 1 az 5)
Vyuzij co nejvic moznoti reseni:
slozene podminky
logicke spojky
rozahy
'''

uzivatel = input("Zadej cele cislo: ")

if uzivatel.isdigit():
    if uzivatel in "1,2,3,4,5":
        print("Jedna se o skolni znamku.")
    else:
        print("Nejedna se o skolni znamku.")
else:
    print("Nejedna se o cislo zkus to znovu.")



'''
Vytvor program dle zadane teploty
vypise jaky je pocitovy stav.
Napr. je telo, je obstojne, je zima.
'''         

teplota = int(input("Zadej teplotu ve stupnich: "))

if teplota > 0 and teplota < 20:
    print("je zima")
else:
    if teplota > 20 and teplota < 30:
        print("je obstojne")
    if teplota in range(30,50):
        print("Vedro")
    else:
        print("Jsi na mimozemske planete.")

'''
Vytvor program ktery postupne 
projde bodove vyledky 5 osob
a spolu se jmenem osoby vypise
kolik bodu a jake hodnoceni osoba ziskala.
'''

osoby = "Petr", "Franta", "Tereza", "Pavel", "Jonas"
body = 15, 7, 10, 21, 43
pocitadlo = len(osoby)
for i in range(pocitadlo):
    print(f"{osoby[i].ljust(7)}= {body[i]:.>5}", end=" ")

    if body[i] in range(0,20):
        print("Podprumerny")
    elif body[i] in range(20,40):
        print("Normalni")
    elif body[i] in range(40,60):
        print("Nejlepsi")

'''
Vytvor program ktery postupne 
projde bodove vyledky 5 osob
a spolu se jmenem osoby vypise
kolik bodu a jake hodnoceni osoba ziskala.
'''

prvni_osoba = 20, 5, 0, 6, 1
druha_osoba = 18, 32, 15, 9, 4
treti_osoba = 5, 2, 8, 9, 15
ctvrta_osoba = 11, 14, 3, 7, 21
pata_osoba = 12, 10, 5, 1, 6

dohromady = prvni_osoba, druha_osoba, treti_osoba, ctvrta_osoba, pata_osoba
paka = sum(prvni_osoba), sum(druha_osoba), sum(treti_osoba), sum(ctvrta_osoba), sum(pata_osoba)
pocitadlo = 0
for i in dohromady:
    vypocet = sum(i)
    if vypocet > pocitadlo:
        pocitadlo = vypocet
print(f"Marek = {sum(prvni_osoba)}\nTomas = {sum(druha_osoba)}\nFranta = {sum(treti_osoba)}\nJakub = {sum(ctvrta_osoba)}\nHanka = {sum(pata_osoba)}")
print(f"Vyhral Tomas = {pocitadlo}")



'''
Vytvor program ktery dle zadaneho
mesice cislem vypise jake momentalni 
rocni obdoby je.
'''
import datetime
dnes = datetime.date.today()
print(f"{dnes}", end=" ")
cislo = input("Zadej cislo mesice: ")
if cislo == "1":
    print("Leden")
else:
    if cislo == "2":
        print("Unor")
    else:
        if cislo == "3":
            print("Brezen")
        else:
            if cislo == "4":
                print("Duben")
            else:
                if cislo == "5":
                    print("Kveten")
                else:
                    if cislo == "6":
                        print("Cerven")
                    else:
                        if cislo == "7":
                            print("Cervenec")
                        else:
                            if cislo == "8":
                                print("Srpen")
                            else:
                                if cislo == "9":
                                    print("Zari")
                                else:
                                    if cislo == "10":
                                        print("Rijen")
                                    else:
                                        if cislo == "11":
                                            print("Listopad")
                                        else:
                                            if cislo == "12":
                                                print("Prosinec")
                                            else:
                                                print("Jsi mimo rozsah")  
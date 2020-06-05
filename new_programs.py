
'''
Pomoci cyklu vypis cisla od -x do +x 
pricemz hodnotu x zada uzivatel.
Cisla budou formatovana, zaporna se dvemi 
desetinnymi misty, nula a kladna zarovnana doprava s 
predrazenymi nulami
'''
cisla = int(input("Zadej cislo x: "))

start = cisla * (-1)
konec = cisla + (1)
if cisla < 0:
    print("Nelze provest")

for i in range(start,konec):
    
    if i < 0:
        print(f"{i:0.2f}")
    else:
        print(f"{i:>010}")


'''
Vytvor algoritmus pro prevod hodnot
zadane v gb na MB a KB, B a bity.
dle SI.
'''
# 1GB = 2^10 MB = 2^20Kb = 2^30B = 2^30  * 8b
prevod = int(input("Zadej velikost v GB: "))

MB = prevod * pow(2,10)
KB= MB * pow(2,10)
B = KB * pow(2,10)
b = B * 8

print(f"{prevod}GB = {MB}Mb = {KB}Kb = {B}Bajtu = {b}bitu")


'''
Vytvor algoritmus pro prevod zadane 
v m na dm, cm, mm, km dle SI
'''
delka = int(input("Zadej delku v km: "))

metr = delka * 10 **3
deci = metr * 10 
centi = deci * 10 
mili = centi * 10 
print(f"{delka:.2e}Km = {metr:.2e}m = {deci:.2e}dm = {centi:.2e}cm = {mili:.2e}mm")



'''
Ve tride je x divek a y chlapcu 
vytvor algoritmus pro vyjadreni 
procentualniho podilu divek a chlapcu
'''
divky = int(input("Zadej pocet divek: "))
chlapci = int(input("Zadej pocet chlapcu: "))
if divky > 0 or chlapci > 0:
    divky_procenta = divky / (divky + chlapci) * 100
    print("Divek",round(divky_procenta),"%","Chlapcu", round(100 - divky_procenta),"%")
else:
    print("Zadej aspon jedno cislo.") 


'''
Vytvor priklad pro zmenu obsahu
dvou promennych. Vstupem jsou 
dve celociselne hodnoty, vystupem
totez. Reseni: s vyuzitim pomocne 
promene nebo postupnym odecitanim.
'''
a = int(input("Zadej hodnotu A: "))
b = int(input("Zadej hodnotu B: "))

c = a
a = b
b = c

print(a,b)   


'''
Vytvor program pro vypocet poplaku za
smenu z CZK na EUR. 
Poplatek cini 1% ze smenovane castky,
minimalni vye poplatku je 50kc.
Stanovte pevny kurz pro prevod.
Vystupem bude vyse poplatku a pocet EUR.
'''

castka = int(input("Zadej pocet CZK: "))
kurz = 25 # 25kc
poplatek = castka / 100
euro = castka / kurz
if poplatek < 50:
    poplatek = 50
   
print(f"Zakaznik dostane {euro:.0f} Euro a zaplati poplatek {poplatek:.0f}Kc.")


'''
Vytvor algoritmus pro rozdeleni
majetku mezi libovolny pocet
potomku.Hodnota majetku bude
zadana v CZK. Vystupem programu bude
celociselna castka v CZK pripadajici na 
1 potomka a nerozdeleny zbytek v CZK.
'''

potomci = int(input("Zadej pocet potomku: "))
majetek = int(input("Zadej hodnotu majetku v CZK: "))
if potomci > 0 and majetek > 0:
    pocet = majetek // potomci 
    zbytek = majetek % potomci
    print(f"Podil: {pocet} Kc \nZbytek: {zbytek} Kc")
else:
    if potomci <= 0:
        print("Nema kdo dedit")
    else:
        print("Nemas zadny majetek na rozdavani.")


'''
Vytvor algoritmus pro posouzeni zda li 
dve vlozene celociselne hodnoty delit 
beze zbytku. Vytupem programu bude jeden ze 
dvou stavu lze delit nelze delit beze zbytku.
'''

hodnota_1 = int(input("Zadej prvni cislo: "))
hodnota_2 = int(input("Zadej druhe cilo: "))


if hodnota_2 != 0:
    zbytek = hodnota_1 % hodnota_2   
    if zbytek == 0:
        print("Ano!")
    else:
        print("Ne!")
else:
    print("Nelze delit nulou")
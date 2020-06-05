'''
Uprav predchozi program znamky
tak aby program hodnoty ukladal do seznamu.
Seznam vypis pred a po setrideni.
Vypis nejlepsi a nejhorsi a prumernou znamku seznamu.
'''


znamky = int(input("Zadej 1. znamku: "))
pocitadlo = 1
seznam = []
if znamky > 0:
    while znamky in range(1,6):
        seznam.append(znamky)
        print(znamky)
        pocitadlo = pocitadlo + 1
        znamky = int(input(f"Zadej {pocitadlo}. znamku: "))
if znamky < 1 or znamky > 6:            
    print(f"Konec programu. \n---------------------------- \nSeznam vsech znamek {seznam}")
    seznam.sort()
    print(f"Seznam vsech serazenych znamek {seznam}")
    print(f"Prumerna znamka je: {round(sum(seznam) / len(seznam))}")
    print(f"Nejvetsi znamka : {max(seznam)} \nNejmensi znamka : {min(seznam)}")
else:
    print("Tohle nejde")



'''
Vytvor algoritmus, ktery do 
seznamu ulozi "x" polozek
seznamu pro nakup.
Kontroluj aby se polozky v seznamu
neopakovaly.
Polozky vypis pred a po setrideni.
'''

kosik = []
nakup = input("Zadej polozky pro nakup zbozi: ")
nakup = nakup.lower()
if nakup.isalpha():
    while nakup != "konec":    
        kosik.append(nakup)
        nakup = input("Zadej polozky pro nakup zbozi: ")
        if nakup in kosik:
            print("Polozka se opakuje")
    kosik.sort()
    neopakovat = set(kosik)          
    print("Musim koupit:", " ".join(neopakovat))
else:
    print("Musis napsat text")
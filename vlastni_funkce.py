# parametricka funkce 
def ctverec(strana):
    '''
    Funkce ktera vypocita obvod ctverce
    '''
    promena = 4 * strana
    return promena


strana = int(input("Zadej stranu: "))
b = ctverec(strana)

print(ctverec.__doc__)
print(b)




# bezparametricka funkce
def sachovice():
    ''' nakresli jedndouche pole sachovnice
    z pismenek "B" a "W" 8x8
    '''
    for i in range(0,8):
        for j in range(0,8):
            if (i + j) % 2 == 0:
                print("B", end=" ")
            else:
                print("W",end=" ")
        print()
        
print(sachovice.__doc__)
odpoved = input("Chces vykreslit sachovnici? Ano/Ne ")
odpoved = odpoved.lower()

while odpoved == "ano":
    sachovice()
    print()
    odpoved = input("Chces vykreslit sachovnici? Ano/Ne ")
    odpoved = odpoved.lower()






def nasobilka(cislo1,cislo2):
    '''
    Vypise nasobilku:
    prvni zadane cislo znamena nasobek
    druhe cislo pak pocet nasobku
    '''

    print()
    for i in range(1,cislo1 + 1):
        for j in range(1,cislo2 + 1):
            vysledek = i * j
            print(f"{vysledek:>4}",end=" ")
        print()

a, b = int(input("Zadej cislo: ")), int(input("Zadej cislo: "))
nasobilka(a,b)

print(nasobilka.__doc__)





def pyramida(cislo):

    ''' Jednoducha funkce na vyrobu pyramid'''

    for i in range(1,cislo + 1):
        print("o" * i )

pocet = int(input("Zadej velikost pyramidy: "))
if pocet > 0:
    pyramida(pocet)
else:
    print("Zadal jsi spatne cislo.")
print()
print(pyramida.__doc__)





def pyramida(cislo):

    ''' Jednoducha funkce na vyrobu pyramid vol.2'''
  
    for i in range(1,cislo + 1):

        print(" " * (cislo - i) + "o " * i)

pocet = int(input("Zadej velikost pyramidy: "))
if pocet > 0:
    pyramida(pocet)
else:
    print("Zadal jsi spatne cislo.")
print()
print(pyramida.__doc__)





def ctverec(strana, znak):
    '''
    vykresleni ctverce podle zvolene strany
    a znaku
    '''

    for i in range(1,strana + 1):
        print((znak + " ") * strana)
       
strana = int(input("Zadej stranu ctverce: "))
znak = input("Zadej znak jakym ma byt ctverec vykreslen: ")

ctverec(strana,znak)


def ctverec(strana):
    for i in range(1, strana + 1):
        if i == 1 or (i == strana):
            print("* " * strana )
        else:
            print("*" + " " * (strana + (strana - 3)) + "*")
    

strana = int(input("Zadej stranu: "))
ctverec(strana)







'''
vypocet medianu podle zadanych hodnot od uzivatele
'''

def median(seznam):
    seznam.sort()
    pocet = len(seznam)
    if pocet % 2 != 0: # vypocet u sudych poctu prvku
        # pocet musime vydelit celociselne dvemi abychom dostali median.
        median = seznam[pocet // 2]

    else:
        # vypocet licheho poctu prvku
        prvek = pocet // 2
        median = (seznam[prvek] + seznam[prvek - 1]) // 2
    return median

seznam = []

pocet = int(input("Zadej pocet cisel v seznamu: "))

for i in range(0,pocet):
    seznam.append(int(input(f"{i + 1}. prvek seznamu: ")))

print(median(seznam))
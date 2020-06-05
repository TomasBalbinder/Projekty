
'''
Hra Sibenice
-------------
Do promene si uloz tajne slovo
a pomocnou promenou si napln
treba hvezdickami (jako mista pro pismena).
Uzivatel pak bude zadavat pismena, pokud bude 
pismeno v tajnem slove, prepis hvezdicku na dane 
pismeno.
Pocitej trestne body.
'''


'''
Udelat hvezdicky
----------------
Vrati retezec(sifru) s tolika
hvezdickami jakou delku 
ma hadane slovo.
'''

'''
Sibenice
--------
uzivatel zada znak
prochazej jednotlive indexy
hadaneho slova, kdyz je znak shodny
s pismenem nahrad index, sifry zadanym znakem.
'''

'''
Hraj Sibenice
--------------
pokud sifra neni shodna se slovem
opakuj cast sibenice
'''
#------------------------------------------------------

retezec_sifra = input("Zadej text: ")
delka = len(retezec_sifra)
hvezdicka = "*"
sifra = delka * hvezdicka
trestne_body = 0

while sifra != retezec_sifra:
    print(sifra)
    zadani_znaku = input("Zadej pismeno: ")
    sifra = list(sifra)
    if zadani_znaku in retezec_sifra:
        for i in range(0,delka):
            if retezec_sifra[i] == zadani_znaku:
                sifra[i] = zadani_znaku                
    else:
        print("Hadej smudlo")
        trestne_body = trestne_body + 1
       
    sifra = "".join(sifra)
    
print(sifra)
print(trestne_body)





 




  
        
    


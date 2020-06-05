kosik = set()
nakup = "" # neni potreba

while True:
    try:
        nakup = input("Zadej polozky pro nakup zbozi: ")
        if nakup in ("konec", ""):
            print("Koncim.")
            break
        
        if not nakup.isalpha():
            print("Nerozumim reci tveho kmene.")
            continue
        
        # Set duplicitu stejne neprida
        #if nakup in kosik:
        #    print("Polozka se opakuje")
        #    continue

        kosik.add(nakup)

    except KeyboardInterrupt:
        print("Ctrl+c, koncim.")
        break

kosik = sorted(kosik) # set nema .sort()

print("Musim koupit:", " ".join(kosik))




cislo = input('Zadej cislo: ')
elementy = ' + '.join(f'{nasobek} * 1{(len(cislo) - mocnina - 1) * "0"}'for mocnina, nasobek in enumerate(str(cislo)))
print(f'{cislo} = ' + elementy)
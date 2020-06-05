
import random

with open('zkouska.txt', 'r') as file:
    data = file.read()

rozdeleni = data.split(" ")


seznam = list()
for i in rozdeleni:
    dalsi = i.split(" ")
    seznam.append(dalsi)

print(seznam)
uzivtel = input("Zadej text: ") 
x = 0
while x < len(seznam) :
    for j in seznam[x]:
        print(j, x)
        if uzivtel == j:
            print(seznam[x])
            x = x + 1
    uzivtel = input("Zadej text: ")
    if uzivtel == "konec":
        break
        




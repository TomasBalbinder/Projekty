
# easy script for change position letter for back to forward
entrance = input("Enter text: ")
letters = list(entrance)
for letter in letters[::-1]:        
    print(letter,end="")




"""
easy program for compared palindroms
"""

entrance = input("Enter text: ")
entrance = entrance.replace(" ", "")
letters = list(entrance)
palindrom = []
for letter in letters[::-1]:
    palindrom.append(letter)
x = "".join(palindrom)
if x == entrance:
    print("Yes, it is palindrom!")
else:
    print("No, its not palindrom!")



'''
program for evaluated first number
'''

number = input("Enter a number: ")

if number.isdigit():
    number = int(number)
    divide = list()
    for i in range(1, number + 1):
        if number % i == 0:
            divide.append(i)
    if len(divide) == 2:
        print(number,"A Number is prime number")
    else:
        print("A Number is not prime number")
else:
    print("Not a number")



"""
Create program whitch going simulation 
play machine. For set characters ♥♦♣♠ 
"""
import random

total_turn = int(input("Enter number of turn: "))
turn_cards = 0
count = 0
list_2 = []
while count < total_turn:
    count += 1

    while True:
        turn_cards += 1
        cards = ["♥", "♦", "♣" ,"♠"]
        list_1 = []

        for i in range(0,3):
            list_1.append(random.choice(cards))
        symbol_1 = " ".join(list_1)
        print(symbol_1)
        print("------")

        if list_1 == ["♥"] * 3 or list_1 == ["♦"] * 3 or list_1 == ["♠"] * 3 or list_1 == ["♣"] * 3:
            list_2.append(symbol_1)
            
            break
        else:
            continue
symbol = ', '.join(list_2)
average = turn_cards / total_turn
print("The computer will randomly done {} turns. and find {}x same symbol. \nAverage all turns is {}.".format(turn_cards, total_turn, average))            
print(f"List all the same symbols: {symbol}")  



'''
This is a game called Bingo
'''     

print()
import random

start = 1
end = 15

player = []
   
for i in range(0,5):
    for j in range(0,5):
        number = random.randint(start, end)
        while number in player:
            number = random.randint(start, end)
        player.append(number)
        print(f"{number:>5}", end='')
    start = start + 15
    end = end + 15
    print()

print()
print("--------------------------\n".rjust(28))


game = []
for k in range(0,25):
    number  = random.randint(1, 75)
    while number in game:
        number = random.randint(1, 75)
    game.append(number)
    print(f"{number:>5}",end="")
    if (k + 1) % 5 == 0:
        print()

summary = []
for l in game:
    if l in player:
        summary.append(l)

        
print(f"  You have {len(summary)} right numbers.")
print(summary)




'''
Create you program which make 
one pair of students randomly 
from the same long list.
'''

import random

boys = ["Honza", "Franta", "Petr", "Kuba", "Tomas", "Janek"]
girls = ["Kristina", "Eliska", "Lucka", "Nikola", "Tereza", "Jana"]

random.shuffle(boys)
random.shuffle(girls)
for i in range(len(boys)):
    print(f"{i + 1}. lavice - {girls[i]} + {boys[i]}")



'''
Create you program which make 
one pair of students randomly 
from the same long list.
'''

import random

boys = ["Honza", "Franta", "Petr", "Kuba", "Tomas", "Janek"]
girls = ["Kristina", "Eliska", "Lucka", "Nikola", "Tereza", "Jana"]

random.shuffle(boys)
random.shuffle(girls)
for i in range(len(boys)):
    print(f"{i + 1}. lavice - {girls[i]} + {boys[i]}")



'''
Create program like giftmaker
people give presents each other
'''

import random

people = ["Zuzka", "Jarda", "Tomas", "Hanka", "Lenka"]
copy = people.copy()

for guy in people:
    who = random.choice(copy)
    while who == guy:
        who = random.choice(copy)
    print(f"{guy} - {who}")
    copy.remove(who)
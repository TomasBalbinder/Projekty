'''
Create a program who writte how many
units, tens, hundreds and thousands make up 
the nubmer on the input

input: natural number 
output: numbers of units, tens, hundreds, thousands

1. read input value 
2. calculation 
3. output
'''

natural_numbers = int(input("Enter the number: "))

output = natural_numbers

ten_thousands = output // 10000
residue = output % 10000
print("You get: %.0f" % ten_thousands,"ten thousands")

thousands = residue // 1000
residue = output % 1000
print("You get: %.0f " % thousands,"thousands")

hundreds = residue // 100
residue = output % 100
print("You get: %.0f " % hundreds,"hundreds")

tens = residue // 10
residue = output % 10
print("You get: %.0f " % tens,"tens")

units = residue // 1
residue = output % 1
print("You get: %.0f " % units,"units")








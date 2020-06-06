'''
Create you program, which separate amount for input
on coins nominal values 50, 20, 10, 5, 2, 1.
On the same principle operate the return machines
The remaining amount after purchase with the difference that
work in a cycle.


input: amount
output: number of coins in CZK currency

1. writte input 
2. sequentially whole division
3. output numbers of coins 
'''


coins = int(input("Enter the amount to split the coin: "))

fifty = coins // 50
residue = coins % 50
twenty = residue // 20
residue = residue % 20
ten = residue // 10
residue = residue % 10
five = residue // 5
residue = residue % 5
two = residue // 2
residue = residue % 2         
one = residue// 1
residue = residue % 1

money = str(coins)

print("For", money + "kc", "you get:"
"\n",fifty,"fifty crown" 
"\n",twenty,"twenty crown"
"\n",ten,"ten crown" 
"\n",five,"five crown"
"\n",two,"two crown"
"\n",one,"one crown")



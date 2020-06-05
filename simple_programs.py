# program for enter a name and attribut of person. 

print("Hello, what is your name?")
name = input()
print("What are you like?")
person_quality = input()
print(f"{name} is {person_quality}.")




#program for exponentiate

whole_number = int(input("Enter a number to exponentiate: "))
print("Result is:",pow(whole_number,2))




# calculation circle radius and content

from math import pi
circle = float(input("Enter a circle radius: "))
print(f"Circle circumference is: {(circle * pi):.3f} cm")
print(f"Circle content is: {(pi * pow(circle,2)):.3f} cm^2")



# easy script for change position letter for back to forward
entrance = input("Enter text: ")
letters = list(entrance)
for letter in letters[::-1]:        
    print(letter,end="")





import os
import time
steps = input("How many steps? ")

number = int(steps) 
top = ("__")
down = number

print(top)    
for num in range(1,number):
     
    kun = "%s|_" % (' ' * num *2)
    print(kun)
    time.sleep(0.08)
    
print((down *("__")) + "|")






             




        
        
    
     






    
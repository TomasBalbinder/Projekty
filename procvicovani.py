for number in [1, 2, 3]:
  print(number)
  for word in ["green", "blue", "red"]:
    print(word)

print("===============")

for number in [1, 2, 3]:
  print(number)
  if number == 2:
    break
  for word in ["green", "blue", "red"]:
    print(word)

print("===============")

# Tady je videt, ze break ve vnitrnim cyklu neukonci cyklus vnejsi
for number in [1, 2, 3]:
  print(number)
  for word in ["green", "blue", "red"]:
    print(word)
    if word == "green":
      break

print("===============")

for number in [1, 2, 3]:
  print(number)
  continue
'''for word in ["green", "blue", "red"]:
    print(word)
'''
print("===============")

for number in [1, 2, 3]:
  print(number)
  for word in ["green", "blue", "red"]:
    print(word)
    continue
    

import random
import itertools

def shuffle_word(word):
  """
  Funkce pro zamichani slova
  Vezme slovo a promicha v nem pismenka
  Neco podobneho si delal i ty
  Dobry je to vytahnout si to do funkce
  """
  word_list = list(word)
  random.shuffle(word_list)
  return "".join(word_list)

words = []
with open('zkouska.txt') as f:
  for word in f:
    words.append(word.strip())

"""
itertools je knihovna, ktera pomaha s tvorenim iteratoru
metoda cycle vezme list a furt dokola ho prochazi
"""
for word in itertools.cycle(words):
  print(f"Uhadnes tohle slovo: {shuffle_word(word)}")
  user_input = input("Zadej slovo: ")
  
  """
  Pokud uzivatel chce skoncit, tak napise slovo konec, prerusi se nejblizsi 
  cyklus - tedy for word in itertools.cycle(words)
  """
  if user_input == "konec":
    break
  
  """
  Dokud se uzivatel netrefi, tak bude probihat nasledujici cyklus
  Chceme ale umoznit uzivateli, aby se hrou prestal, kdyz neco uhodne 
  spatne - proto stejna podminka jako vyse
  Nicmene tim breakem prerusime jenom nejblizsi cyklus - tedy while cyklus
  a cyklus for word in itertools.cycle(words) by probihal dal
  Proto je tam konstrukce:
  else:
  
  """
  while word != user_input:
    if user_input == "konec":
      break
    print("Spatne, zkus to znovu.")
    user_input = input("Zadej slovo: ")
  else: # tahle vetev se vykona, kdyz ve while nebude break
    continue
  break # tady prerusime uz vnejsi cyklus for word in intertools.cycle(words)


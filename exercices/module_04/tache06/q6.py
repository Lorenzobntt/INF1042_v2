import random

eleves = {"Alexandre", "Lorenzo", "Yonas", "Sebastian",
          "Liam", "Joshua", "Ben", "Hansel", "Elisee",
          "Verlaine", "Miguel", "Roman", "Edwin", "Alexander"}

while eleves:
    nom = random.choice(list(eleves))
    print(nom)
    eleves.remove(nom)
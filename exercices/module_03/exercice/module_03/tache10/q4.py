
import random

n = int(input("Nombre de tirages : "))

if n > 0:
    compteurs = [0, 0, 0, 0]

    for i in range(n):
        nombre = random.randint(1, 4)
        compteurs[nombre - 1] += 1

    for i in range(4):
        pourcentage = compteurs[i] / n * 100
        print(i + 1, ":", compteurs[i], "fois,", round(pourcentage, 2), "%")

    plus = compteurs.index(max(compteurs)) + 1
    print("Nombre le plus tire :", plus)
else:
    print("Nombre invalide")

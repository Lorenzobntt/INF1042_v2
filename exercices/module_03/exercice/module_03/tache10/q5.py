
import math

electrique = input("Voiture electrique ? oui/non : ")
duree = float(input("Nombre d'heures : "))

if duree <= 0:
    print("Duree invalide")
else:
    heures = math.ceil(duree)

    prix = 4 + (heures - 1) * 2.50

    if prix > 20:
        prix = 20

    rabais = 0

    if electrique == "oui":
        rabais = prix * 0.20

    total = prix - rabais

    print("Duree :", duree)
    print("Heures facturees :", heures)
    print("Prix :", f"{prix:.2f}")
    print("Rabais :", f"{rabais:.2f}")
    print("Total :", f"{total:.2f}")
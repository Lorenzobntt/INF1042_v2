
montant = float(input("Montant de l'achat : "))

if montant < 50:
    rabais = 0
elif montant <= 100:
    rabais = 5
else:
    rabais = 10

economie = montant * rabais / 100
sous_total = montant - economie
taxe = sous_total * 0.13
total = sous_total + taxe

print("Montant initial :", f"{montant:.2f}")
print("Rabais :", rabais, "%")
print("Economie :", f"{economie:.2f}")
print("Sous-total :", f"{sous_total:.2f}")
print("Taxe :", f"{taxe:.2f}")
print("Total :", f"{total:.2f}")
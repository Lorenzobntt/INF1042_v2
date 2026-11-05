
import random

prenom = input("Prénom : ")
nom = input("Nom : ")
annee = input("Année de naissance : ")
ville = input("Ville : ")

identifiant = prenom + "." + nom + "@" + ville + ".ca"

motdepasse = prenom[:2] + nom[:2] + annee[-2:]

for i in range(4):
    motdepasse += str(random.randint(0, 9))

print("Identifiant :", identifiant.lower())
print("Mot de passe :", motdepasse)
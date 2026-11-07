nom = input("Ton nom : ")

if len(nom) < 8 or len(nom) > 12:
    print("Erreur")
else:
    print("Nom valide")
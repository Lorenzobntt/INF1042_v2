
nombres = []

try:
    with open("valeurs.txt", "r") as fichier:
        for ligne in fichier:
            nombres.append(int(ligne.strip()))

    if len(nombres) > 0:
        print("Maximum :", max(nombres))
        print("Minimum :", min(nombres))
        print("Moyenne :", sum(nombres) / len(nombres))
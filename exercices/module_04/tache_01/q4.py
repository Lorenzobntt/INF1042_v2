
phrase = input("Écris une phrase : ")

mots = phrase.split()
print("Liste des mots :", mots)
print("Nombre de mots :", len(mots))

nouvelle_phrase = "-".join(mots)
print(nouvelle_phrase)


phrase = input("Écris une phrase : ")

nombre = 0

for lettre in phrase.lower():
    if lettre in "aeiouy":
        nombre = nombre + 1

print("Nombre de voyelles :", nombre)
matchs = (
    ("Tigres", "Lynx", 25, 18),
    ("Aigles", "Panthères", 22, 25),
    ("Tigres", "Panthères", 25, 23),
    ("Lynx", "Aigles", 19, 25),
    ("Tigres", "Aigles", 21, 25),
    ("Lynx", "Panthères", 25, 20)
)

equipes = ("Tigres", "Lynx", "Aigles", "Panthères")

gagnants = []
perdants = []
victoires = []
points = []

for e1, e2, s1, s2 in matchs:
    if s1 >  s2:
        print("Les", e1, "ont battu les", e2, "par", s1, "à", s2")
        gagnants.append(e1)
        perdants.append(e2)

        print(e, "a autant de victoires que de défaites")
    else:
        print(e, "a plus de défaites que de victoires")


        #je n ai pas reussit a faire ca
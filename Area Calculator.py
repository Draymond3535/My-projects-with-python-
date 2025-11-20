import math

print("Calculateur de surface 📐")
print("1) Triangle")
print("2) Rectangle")
print("3) Carré")
print("4) Cercle")
print("5) Quitter")

fig = int(input("Quelle forme choisissez-vous : "))

a = 1
b = 2
c = 3
d = 4
e = 5

if fig == a:
    ba = float(input("Base : "))
    he = float(input("Hauteur : "))
    area = (ba * he) / 2
    print("La surface du triangle est :", area)

elif fig == b:
    le = float(input("Longueur : "))
    wi = float(input("Largeur : "))
    area_2 = le * wi
    print("La surface du rectangle est :", area_2)

elif fig == c:
    co = float(input("Côté : "))
    area_3 = co ** 2
    print("La surface du carré est :", area_3)

elif fig == d:
    ra = float(input("Rayon : "))
    area_4 = math.pi * (ra ** 2)
    print("La surface du cercle est :", area_4)

elif fig == e:
    print("Au revoir ! 👋")

else:
    print("Erreur. Veuillez réessayer.")

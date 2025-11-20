print("Bienvenue dans le calculateur d'interet")
print("Choisis ce que vous voulez faire : ")
print("1.Avoir le montant final avec le taux d'interet simple ")
print("2.Avoir le montant final avec le taux d'interet compose ")
user= int(input("Choisis le taux (1-2):  "))
#Taux simple
if user== 1 : 
    C=float(input("Quel est ton capital (en fcfa) ?"))
    t=float(input("Quel est le taux (en %) ?"))
    d=float(input("Quel est la durée (en année)?"))
    t=t/100
    A_1 = C * (1 + d * t)
    I= C *t*d 
    print("Vous aurez  ",A_1 , "de fcfa, a la fin de cet investissement.")
    print(" Et les intérêts gagnés sont de ",I,"fcfa")
    # Taux compose 
elif user ==2 : 
    P = float(input("Capital initial : "))
    r = float(input("Taux d'intérêt (en %) : ")) / 100
    n = int(input("Nombre de périodes : "))
    A_2= P *(1+r)**n
    In= A_2- P
    print("Vous aurez",A_2 , "fcfa , a la fin de cet investissement.")
    print("Et les intérêts gagnés sont de ",In,"fcfa")
print("Merci pour ta participation ")
    


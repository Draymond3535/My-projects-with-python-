print("Bienvenue dans mon secteur privé, où tous vos rêves deviennent réalité 🌟")
print("Choisissez ce que vous voulez convertir :")
print("1. Convertir Celsius en Kelvin")
print("ou")
print("2. Convertir Kelvin en Celsius")

user = int(input("1 ou 2 : "))

if user == 1: 
    c = float(input("Quelle est la température en Celsius : "))
    total = c + 273.15
    print("La température en Kelvin est :", total, "K")
    
elif user == 2:
    d = float(input("Quelle est la température en Kelvin : "))
    total_2 = d - 273.15
    print("La température en Celsius est :", total_2, "°C")

print("Merci pour votre participation ! 😊")

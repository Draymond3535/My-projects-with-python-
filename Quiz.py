# Instruction
print("Bienvenue sur notre quiz à choix multiples ")
print("Ce quiz comporte 3 parties notamment : ")
print("1. Questions à choix multiples ")
print("2. Quiz Vrai ou Faux ")
print("Voici comment les points seront distribués par partie: ")
print("- Questions à choix multiples : Chaque question vaut 5 points étant donné qu'il y a 5 questions ")
print("- Quiz : Vrai ou Faux  : Chaque question vaut 1 point étant donné qu'il y a 5 questions ")
print("À la fin de cette expérience, le résultat vous sera donné ")
print("Profitez de cette magnifique expérience et bonne chance ! 😊😊")

# SCORE
total = 0

# Question 1
print("1. Quelle est la capitale de la France ?")
print("a) Madrid")
print("b) Paris")
print("c) Rome")
print("d) Berlin")
ans_1 = input("Choisis ta réponse (a-d) : ").lower()

if ans_1 == "b":
    total += 5

# Question 2
print("2. Quel est l’élément chimique représenté par 'O' ?")
print("a) Or")
print("b) Oxygène")
print("c) Osmium")
print("d) Ozone")
ans_2 = input("Choisis ta réponse (a-d) : ").lower()

if ans_2 == "b":
    total += 5

# Question 3
print("3. Quel est l’élément le plus abondant dans l’univers ?")
print("a) Oxygène")
print("b) Carbone")
print("c) Hydrogène")
print("d) Hélium")
ans_3 = input("Choisis ta réponse (a-d) : ").lower()

if ans_3 == "c":
    total += 5

# Question 4
print("4. Quelle est la planète la plus proche du Soleil ?")
print("a) Terre")
print("b) Vénus")
print("c) Mercure")
print("d) Mars")
ans_4 = input("Choisis ta réponse entre a et d : ").lower()

if ans_4 == "c":
    total += 5

# Question 5
print("5. Quel pays a remporté la Coupe du Monde 2018 ?")
print("a) Brésil")
print("b) Allemagne")
print("c) France")
print("d) Argentine")
ans_5 = input("Choisis ta réponse entre a et d : ").lower()

if ans_5 == "c":
    total += 5

print()
print("=== Score final ===")
print("Tu as obtenu :", total, "/ 25")

# Questions Vrai ou Faux
print("Passons aux choses sérieuses : ")
print("Question Vrai ou Faux : ")

# Score
total_2 = 0
v = "Vrai"
f = "Faux"

# Question 1
print("1. La Terre est plus proche du Soleil que Vénus.")
print(v)
print(f)
ans_2_1 = input("Choisis entre 'Vrai' ou 'Faux': ").capitalize()

if ans_2_1 == f:
    print("Correct, Vénus est plus proche du Soleil que la Terre")
    total_2 += 1
elif ans_2_1 == v:
    print("Incorrect, Vénus est plus proche du Soleil que la Terre")
else:
    print("Erreur")

# Question 2
print("L’eau bout à 100°C à pression atmosphérique normale.")
print(v)
print(f)
ans_2_2 = input("Choisis entre 'Vrai' ou 'Faux': ").capitalize()
if ans_2_2 == v:
    print("Correct !!")
    total_2 += 1
elif ans_2_2 == f:
    print("Incorrect")
else:
    print("Erreur")

# Question 3
print("La lumière voyage plus lentement dans le vide que dans l’air.")
print(v)
print(f)
ans_2_3 = input("Choisis entre 'Vrai' ou 'Faux': ").capitalize()
if ans_2_3 == v:
    print("Incorrect")
elif ans_2_3 == f:
    print("Correct !!")
    total_2 += 1
else:
    print("Erreur")

# Question 4
print("L’ADN se trouve uniquement dans le noyau des cellules.")
print(v)
print(f)
ans_2_4 = input("Choisis entre 'Vrai' ou 'Faux': ").capitalize()
if ans_2_4 == v:
    print("Incorrect")
elif ans_2_4 == f:
    print("Correct !!")
    total_2 += 1
else:
    print("Erreur")

# Question 5
print("Les poissons respirent grâce aux poumons.")
print(v)
print(f)
ans_2_5 = input("Choisis entre 'Vrai' ou 'Faux': ").capitalize()
if ans_2_5 == v:
    print("Incorrect")
elif ans_2_5 == f:
    print("Correct !!")
    total_2 += 1
else:
    print("Erreur")

print("Ton score total est :", total_2)
print("Score total général :", total + total_2, "/ 30")
print("J'espère que tu as aimé ce petit quiz!")

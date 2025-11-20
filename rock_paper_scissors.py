import random

print("🌟 Bienvenue dans le jeu Pierre-Papier-Ciseaux ! 🌟")
print("✨ Que le meilleur gagne... ou survive 😈 ✨")

a = "✊ Pierre"
b = "✋ Papier"
c = "✌️ Ciseaux"

print("\nChoisis ton arme légendaire :")
print("1)", a)
print("2)", b)
print("3)", c)

player = int(input("➡️ Entre ton choix (1-3) : "))
computer = random.randint(1,3)

if player == 1:
    print("\n🧑 Tu as brandi :", a, "🔥")
elif player == 2:
    print("\n🧑 Tu dégaines :", b, "✨")
elif player == 3:
    print("\n🧑 Tu sors :", c, "⚡")
else:
    print("❌ Choix invalide !")
    exit()


if computer == 1:
    print("🤖 L'ordinateur utilise :", a, "💥")
elif computer == 2:
    print("🤖 L'ordinateur lance :", b, "🌪️")
elif computer == 3:
    print("🤖 L'ordinateur joue :", c, "⚔️")


print("\n⚔️ Résultat du duel :")

if player == computer:
    print("😐 Match nul ! Le combat est trop serré... Réessayez !")

elif player == 1 and computer == 3:
    print("🔥 BOUM ! Pierre écrase Ciseaux ! Tu remportes ce duel ⚡")
elif player == 2 and computer == 1:
    print("💫 Papier enveloppe Pierre ! Tu gagnes avec classe ✨")
elif player == 3 and computer == 2:
    print("⚡ Ciseaux tranchent Papier ! Victoire éclatante ! 💥")

else:
    print("💀 Aïe... L'ordinateur te terrasse cette fois-ci. Garde la tête haute !")


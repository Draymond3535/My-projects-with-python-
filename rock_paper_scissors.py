# Write code below 💖

import random 

print("Rock Paper Scissors")

a = "✊"
b = "✋"
c = "✌️"

print("1)", a)
print("2)", b)
print("3)", c)

player = int(input("Pick a number (1-3): "))

computer = random.randint(1,3)

# Show choices
if player == 1:
    print("You chose:", a)
elif player == 2:
    print("You chose:", b)
elif player == 3:
    print("You chose:", c)

if computer == 1:
    print("The computer chose:", a)
elif computer == 2:
    print("The computer chose:", b)
elif computer == 3:
    print("The computer chose:", c)

# Game logic
if player == computer:
    print("It is a tie!")

elif player == 1 and computer == 3:
    print("You won!")
elif player == 2 and computer == 1:
    print("You won!")
elif player == 3 and computer == 2:
    print("You won!")

else:
    print("You lost!")
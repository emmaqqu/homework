# Lesson 7
# importing
from random import randrange

# input
difficulty = int(input("Enter the DC: "))

# processing & output
roll = randrange(1, 21)

print(f"The player has rolled {roll} on their D20")

if player_roll >= difficulty:
    print("The player was successful")
else:
    print("The player was not successful")
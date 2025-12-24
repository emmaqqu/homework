# Lesson 8

# input
win_counter = 0
for i in range(6):
    current_result = input(f"Enter the game {i+1} results: ")

    if current_result == "W":
        win_counter += 1

group = 0
if win_counter > 4:
    group = 1
elif win_counter > 2:
    group = 2
elif win_counter > 0:
    group = 3

if group == 0:
    print("Player is eliminated")
else:
    print(f"Player is in group {group}")
# Lesson 4
from math import ceil
s1_plank = input("Enter 'F' for each fence plank in section 1: ")
s2_plank = input("Enter 'F' for each fence plank in section 2: ")
s3_plank = input("Enter 'F' for each fence plank in section 3: ")

cans = len(s1_plank) + len(s2_plank) + len(s3_plank)

boxes = ceil(cans / 12)
leftover = 12 * boxes - cans
total_cost = boxes * 14.95

print(f"You need {cans} cans, {leftover} cans leftover, and it will cost you {total_cost}")
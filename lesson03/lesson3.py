# Lesson 3
# answer = tiles ** 0.5

tiles = int(input("Enter the # of tiles: "))

from math import sqrt, floor
answer = floor(sqrt(tiles))

print(f" The side length of the square is {answer}")
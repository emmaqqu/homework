# Lesson 12

def triangletype(x, y, z):
    if x + y + z != 180:
        print("not a triangle")
    elif x == 60 and y == 60:
        print("equilateral")
    elif x != y and x != z and y != z:
        print("scalene")
    else:
        print("isoceles")

triangletype(40, 60, 80)
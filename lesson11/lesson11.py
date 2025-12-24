# Lesson 11

def quadrants(x, y):
    if x > 0 and y > 0:
        print("Quadrant 1")
    elif x > 0 and y < 0: 
        print("Quadrant 4")
    elif x < 0 and y > 0:
        print("Quadrant 2")
    else:
        print("Quadrant 3")

quadrants(5, -2)
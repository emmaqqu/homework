# Lesson 23

def average():
    flag = True
    total = 0
    counter = 0

    while flag:
        mark = input("Enter mark or 'exit'")
        if mark == "exit":
            flag = False
        else:
            grade = int(mark)
            if grade >= 0 and grade <= 100:
                total += grade
                counter += 1
    
    avg = total / counter 
    return avg
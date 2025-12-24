# Lesson 17

def factorial(num):
    i = num - 1
    while i > 0:
        total = num * i
        num = total
        i -= 1
    return total

print(factorial(12))
# Lesson 19
def isprime(num):
    i = num - 1
    while i > 1:
        if num <= 1:
            return False
        elif num % i == 0:
            return False
        else:
            i -= 1
    return True
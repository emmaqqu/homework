# Lesson 22

def fibonnaci(num):
    fib_0 = 0
    fib_1 = 1
    fib_n = 0 # variable initialization

    for value in range(2, num+1):
        fib_n = fib_1 + fib_0
        fib_0 = fib_1
        fib_2 = fib_n
        
    return fib_n
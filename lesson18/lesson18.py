# Lesson 18
def factorsyay(num):
    import math
    start = 1
    new_stop = int(math.sqrt(num)) + 1
    factor_count = 0

    while start < new_stop:
        if num % start == 0:
            dividend = num // start
            if start != dividend:
                factor_count += 2
               # start and dividend are factors of num
            else:
                factor_count += 1
        start += 1

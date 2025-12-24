# Lesson 25

# def largestprimefactor(num):
#     if num <= 1:
#         return False
#     else:
#         highest_factor = 0
#         for i in range(1, num+1):
#             if num % i == 0:
#                 current_factor = num / i
#                 for j in range(1, current_factor+1):
#                     if current_factor % j == 0:
#                         if current_factor == 1 or current_factor == num:  
#                             if current_factor > highest_factor:
#                                 highest_factor = current_factor
#     return highest_factor      

# print(largestprimefactor(360))

# def largestprimefactor(num):
#     if num <= 1:
#         return False
#     for i in range(1, num+1):
#         for j in range(1, num+1):
#             if i % j == 0:
#                 factor1 = i
#                 factor2 = j
#                 if factor1 == 1 or factor1 == num:
#                     if factor2 == 1 or factor2 == num:
#                         if factor1 > factor2:
#                             highest = factor1
#                         else:
#                             highest = factor2
#     return highest



def biggestprimefactor(num):
    list_factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            list_factors.append(i)
    prime_factors = []
    for factor in list_factors:
        for i in range(2, factor):
            if factor % i == 0:
                break
        else:
            prime_factors.append(factor)
    return max(prime_factors)

print(biggestprimefactor(360))
# Lesson 33

def centraltendency(listy):
    freq = len(listy) 
    mean = sum(listy) / freq
    sortedver = sorted(listy)
    mid = freq // 2
    if freq % 2 == 0:
        median = (listy[mid] + listy[mid - 1]) / 2
    else:
        median = sortedver[mid]
    return mean, median

print(centraltendency([3, 4, 5, 1, 2]))
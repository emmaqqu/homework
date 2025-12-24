# Lesson 30
def pattern(num):
    patterns = ""
    for line in range(1, num+1):
        if line % 2 == 0: 
            patterns += "0"
        else:
            patterns += "1"
        print(patterns)

pattern(5)
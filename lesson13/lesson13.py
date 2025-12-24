# Lesson 13
def specialornah():
    month = int(input(""))
    day = int(input(""))
    if month in range(1, 13):
        if month == 2 and day == 18:
            print("Special")
        elif month == 2 and day < 18:
            print("Before")
        elif month == 2 and day > 18:
            print("After")
        elif month < 2:
            print("Before")
        else:
            print("After")

specialornah()
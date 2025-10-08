# Lesson 10
def is_telemarketer(first, second, third, fourth):
    if first == 8 or first == 9:
        if fourth == 8 or fourth == 9:
            if second == third:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

first = int(input("Enter the first digit: "))
second = int(input("Enter the second digit: "))
third = int(input("Enter the third digit: "))
fourth = int(input("Enter the fourth digit: "))
if is_telemarketer(first, second, third, fourth):
    print("ignore")
else:
    print("answer")

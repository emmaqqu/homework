# Lesson 24

def namelength()
    longest_length = 0
    longest_name = ""
    loop = True
    while loop:
        name = input("Enter name or 'x' to exit")
        if name == "x":
            loop = False
        else:
            current_length = len(name)
            if current_length > longest_length:
                longest_length = current_length
                longest_name = name
    return longest_name
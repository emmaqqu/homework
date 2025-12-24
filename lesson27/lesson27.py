# Lesson 27

def alphaonly(word):
    cleanedver = ""
    for character in word:
        if character.isalpha():
            cleanedver += character
    return cleanedver

print(alphaonly("iuhasd712"))
# Lesson 29
def consonants(word):
    vowels = "aeiouy"
    returned = ""
    word = word.lower().replace(" ", "")
    for character in word:
        if character.isalpha() and character not in vowels:
            returned += character
    return returned

print(consonants("i want to eat"))
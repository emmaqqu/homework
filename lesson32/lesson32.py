# Lesson 32

def sorted(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    if not word1 or not word2:
        return []
    else:
        set_word1 = set(word1)
        set_word2 = set(word2)
        result = []
        for character in word1:
            if character in word2:
                result.append(character)
        return sorted(result)

 
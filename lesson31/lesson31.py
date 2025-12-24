# Lesson 31

def anagrams(word1, word2):
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")
    freq_table = {} # empty dict
    for c in word1:
        if c in freq_table:
            freq_table[c] += 1
        else: 
            freq_table[c] = 1
    for c in word2:
        if c not in freq_table:
            return False
        else:
            freq_table[c] -= 1
            if freq_table[c] < 0:
                return False
    for key, value in freq_table.items():
        if value != 0:
            return False
    return True
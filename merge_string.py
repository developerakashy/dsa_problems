def merge_alternative(word1, word2):
    i, j = 0, 0

    merged = ""

    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged += word1[i]
            i += 1
        if j < len(word2):
            merged += word2[j]
            j += 1

    return merged


word1 = 'abcde'
word2 = 'pqrs'

print(merge_alternative(word1, word2))

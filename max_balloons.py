def max_balloons(text):
    char_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

    for char in text:
        if char in char_count:
            char_count[char] += 1

    count = 0
    while char_count['b'] > 0:
        for char in char_count:
            if char == 'l' or char == 'o':
                if char_count[char] < 2:
                    return count
                char_count[char] -= 2
                continue

            if char_count[char] < 1:
                return count

            char_count[char] -= 1

        count += 1

    return count

def easy(text):
    char_count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

    for char in text:
        if char in char_count:
            char_count[char] += 1

    count = min(char_count['b'], char_count['a'], char_count['l']//2, char_count['o']//2, char_count['n'])

    return count


text = "loonbaxbpoon"
text1 = "balllllllllllloooooooooon"

print(max_balloons(text1))
print(easy(text1))

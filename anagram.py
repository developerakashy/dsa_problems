def anagram(s, t):
    s_dict = {}

    for char in s:
        if char in s_dict:
            s_dict[char] += 1
        else:
            s_dict[char] = 1

    for char in t:
        if char not in s_dict:
            return False

        s_dict[char] -= 1

        if s_dict[char] == 0:
            del s_dict[char]

    return not s_dict

s = 'anagram'
t = 'nagram'

print(anagram(s, t))

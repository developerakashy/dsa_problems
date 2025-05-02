def ransome_note(magazine, ransomeNote):
    magz = {}
    for char in magazine:
        magz[char] = magz.get(char, 0) + 1

    for char in ransomeNote:
        if not magz.get(char):
            return False

        magz[char] -= 1

    return True

ransomeNote = 'aa'
magazine = 'abb'

print(ransome_note(magazine, ransomeNote))

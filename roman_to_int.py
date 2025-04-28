def roman_to_int(s):
    R = {
        'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
    }

    num = 0
    for i in range(len(s) - 1):
        if R[s[i]] >= R[s[i+1]]:
            num += R[s[i]]
        else:
            num -= R[s[i]]


    num += R[s[-1]]

    return num

s = "MCMXCIV" #1994

print(roman_to_int(s))

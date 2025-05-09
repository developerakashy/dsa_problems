def valid_palindrome(s):
    string = "".join([x.lower() for x in s if x.isalnum()])

    if string == "":
         return True

    left = 0
    right = len(string) - 1
    while left <= right:
        if string[left] != string[right]:
            return False

        left, right = left + 1, right - 1

    return True


text = 'A man, a plan, a canal: Pnama'
print(valid_palindrome(text))

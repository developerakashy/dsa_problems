def isPalindrome(A):
        if A < 0:
            return 0

        num = A
        reversed = ''
        while num > 0:
            temp = num % 10
            num = num // 10
            reversed += str(temp)

        if int(reversed) == A:
            return 1
        return 0

print(isPalindrome(0))

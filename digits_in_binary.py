def digits_in_binary(n):
    curr = n
    bs = ''
    while curr:
        bs = str(curr%2) + bs

        curr = curr // 2

    return bs

n = 6
print(digits_in_binary(n))

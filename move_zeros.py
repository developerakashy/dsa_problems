def move_zero(A):

    pos = 0

    for i in range(len(A)):
        if A[i] != 0:
            A[pos], A[i] = A[i], A[pos]
            pos += 1

    return A



A = [0, 1, 0, 3, 12]

print(move_zero(A))

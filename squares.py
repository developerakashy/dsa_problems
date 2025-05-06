def squares(A):
    squared = [0] * len(A)

    for i in range(len(A)):
        squared[i] = A[i]*A[i]

    squared.sort()
    return squared

A = [-6, -3, -1, 2, 4, 5]
print(squares(A))

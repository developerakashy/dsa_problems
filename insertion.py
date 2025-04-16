A = [25,17,31,13,2]

def insertion(A):

    for i in range(0, len(A)):
        for j in range(i, 0, -1):
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
            else:
                break

    return A

print(insertion(A))

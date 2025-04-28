def duplicates(A): #O(n^2)
    copy = [A]

    for i in range(len(A)):
        ele = A[i]
        for j in range(len(A)):
            if j == i:
                continue

            if A[i] == A[j]:
                return i, j

A = [1,2,4,5,1,5,7,7]
print(duplicates(A))


def optimal_duplicates(A): #O(n)
    h = {}

    for i in range(len(A)):
        if A[i] in h:
            return (h[A[i]], i)

        h[A[i]] = i

    return False

print(optimal_duplicates(A))

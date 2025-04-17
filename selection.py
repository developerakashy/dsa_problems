def selection(A):
    n = len(A)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if A[min_index] > A[j]:
                min_index = j

        A[i], A[min_index] = A[min_index], A[i]

    return A


A = [-3, -2, 2, 5, 34, 23, 0]
print(selection(A))

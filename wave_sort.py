def wave_sort(A):
    n = len(A)

    A.sort()
    for i in range(0,n - 1, 2):
        A[i], A[i+1] = A[i+1], A[i]


    return A

A = [2, 1]
print(wave_sort(A))

def quick_sort(A):
    n = len(A)

    if n <= 1:
        return A


    pivot = A[-1]

    l = []
    r = []

    for i in range(n-1):
        if A[i] <= pivot:
            l.append(A[i])
        else:
            r.append(A[i])




    return quick_sort(l) + quick_sort([pivot]) + quick_sort(r)

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
print(quick_sort(A))

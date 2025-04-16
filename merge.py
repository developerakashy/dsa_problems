def merge_sort(A):
    n = len(A)

    if n == 1:
        return A

    m = len(A) // 2

    L = A[:m]
    R = A[m:]

    L = merge_sort(L)
    R = merge_sort(R)

    L_len = len(L)
    R_len = len(R)
    l = r = 0

    sorted_arr = [0] * n
    i = 0

    while r < R_len and l < L_len:
        if L[l] < R[r]:
            sorted_arr[i] = L[l]
            l += 1
        else:
            sorted_arr[i] = R[r]
            r += 1

        i += 1

    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l]
        l += 1
        i += 1

    return sorted_arr


print(merge_sort([23,12,45,12,6]))

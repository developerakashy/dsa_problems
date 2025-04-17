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


print(merge_sort([23,12,45, 45,12,6]))


def merge(A):
    n = len(A)

    if n == 1:
        return A

    half = n // 2

    L = merge(A[:half])
    R = merge(A[half:])

    l = len(L)
    r = len(R)

    temp_l = 0
    temp_r = 0

    new_arr = []
    while temp_l < l and temp_r < r:
        if L[temp_l] < R[temp_r]:
            new_arr.append(L[temp_l])
            temp_l += 1
        else:
            new_arr.append(R[temp_r])
            temp_r += 1

    while temp_l < l:
        new_arr.append(L[temp_l])
        temp_l += 1

    while temp_r < r:
        new_arr.append(R[temp_r])
        temp_r += 1


    return new_arr

print(merge([26, 62, 62, -11, 76]))

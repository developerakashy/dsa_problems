def counting_sort(A):
    n = len(A)
    maxx = max(A)

    counts = [0] * (maxx + 1)

    for num in A:
        counts[num] += 1

    i = 0
    for c in range(len(counts)):

        while counts[c] > 0:
            A[i] = c
            i+=1
            counts[c] -= 1

    return A

A = [1, 2, 2, 8, 3, 3, 3, 5, 7]
print(counting_sort(A))

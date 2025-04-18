def interavls(A):
    n = len(A)

    A.sort(key=lambda x:x[0])

    merge = []
    start, end = A[0].start

    for i in range(n):
        curr_start, curr_end = A[i]
        if curr_start >= end:
            end = curr_end
        elif curr_start > end:
            merge.append([start, end])
            start = curr_start
            end = curr_end

    merge.append([start, end])

    return merge

A = [ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ]


print(interavls(A))

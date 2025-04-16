from bisect import bisect_left
A = [ 18468, 6335, 26501, 19170, 15725, 11479, 29359, 26963, 24465, 5706, 28146, 23282, 16828, 9962, 492, 2996, 11943, 4828, 5437, 32392, 14605 ]


# def triplet(A):
#     max_sum = 0

#     for i in range(len(A)-2):
#         for j in range(i+1, len(A)-1):
#             for k in range(i+2, len(A)):
#                 if A[i]<A[j] and A[j]<A[k]:
#                     max_sum = max(max_sum, A[i]+A[j]+A[k])


#     return max_sum

def triplet(A):
    max_sum = 0
    n = len(A)

    for j in range(0,n-1):
        left_max = 0

        for i in range(0, j):
            if A[i] < A[j]:
                left_max = max(left_max, A[i])

        right_max = 0

        for k in range(j+1, n):
            if A[k] > A[j]:
                right_max = max(right_max, A[k])

        if right_max != 0 and left_max != 0:
            max_sum = max(max_sum, left_max + right_max + A[j])

    return max_sum

#!/usr/bin/python
# -*- coding: utf-8 -*-
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i:
        return i - 1
    else:
        return -1





def solve(A):
    n = len(A)
    suffMax = [0] * n
    suffMax[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        suffMax[i] = max(suffMax[i + 1], A[i])
    lst = []
    maxe = 0
    lst.append(A[0])
    for i in range(1, n - 1):
        res = BinarySearch(lst, A[i])
        if res != -1 and A[i]<suffMax[i+1]:
            ans = lst[res] + A[i] + suffMax[i + 1]
            maxe = max(maxe, ans)
        lst.insert(res + 1, A[i])
    return maxe



print(triplet(A))
print(solve(A))

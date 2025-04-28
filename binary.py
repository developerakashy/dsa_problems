A = [-3, -1, 0, 1, 4, 7]

# if -1 in A:
#     print(True) #O(N)

def binary_search(A, target): #O(log n)
    L = 0
    R = len(A) - 1

    while L <= R:
        M = (L+R)//2
        if A[M] == target:
            return True

        elif A[M] < target:
            L = M + 1

        else:
            R = M - 1

    return False

print(binary_search(A, 1))

B = [False, False, False, False, True, True, True]

def binary_search_condition(B):
    L = 0
    R = len(B) - 1

    while L < R:
        M = (L+R)//2
        if B[M]:
            L = M + 1
        else:
            R = M

    return R

print(binary_search_condition(B)) #Got starting index 4 not 5

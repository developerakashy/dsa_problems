B = [False, False, False, True, True, True, True] #monotonic array

def first_bad_version(B):
    L = 0
    R = len(B) - 1

    while L < R:
        M = (L+R)//2
        if B[M]:
            R = M
        else:
            L = M + 1

    return R

print(first_bad_version(B)) #Got starting index 4 not 5

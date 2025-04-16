A = [ 0, 0, 0, 1, 0]
B = 3


# Formula = [X-B+1, X+B-1]

def light(A):
    N = len(A)
    i = 0
    count = 0

    while i < N:
        left = max(0, i - B + 1)
        right = min(N - 1, i + B - 1)

        found = False
        for j in range(right, left - 1, -1):
            if A[j] == 1:
                count += 1
                i = j + B
                found = True
                break

        if not found:
            return -1

    return count

print(light(A))

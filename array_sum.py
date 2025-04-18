def array_sum(A, B):
    arr = list(map(int, (list(str(int("".join(map(str, A))) + int("".join(map(str, B))))))))

    return arr

A = [1,2,4]
B = [2,3,4]

print(array_sum(A, B))

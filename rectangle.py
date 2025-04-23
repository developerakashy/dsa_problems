def rectangle(A, B, C, D):
    d = {}

    d[A] = d.get(A, 0) + 1
    d[B] = d.get(B, 0) + 1
    d[C] = d.get(C, 0) + 1
    d[D] = d.get(D, 0) + 1

    if len(d) == 2:
        keys = list(d.valued())
        if keys[0] == keys[1]:
            return 1

    return 0

print(rectangle(1,2,2,1))

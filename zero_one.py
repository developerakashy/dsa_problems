def zero_one(A):

        counts = [0, 0]

        for num in A:
            if num == 0:
                counts[0] += 1
            else:
                counts[1] += 1
        print(counts)

        return [0] * counts[0] + [1] * counts[1]

A = [0, 1, 0, 0, 1, 1, 1]

print(zero_one(A))

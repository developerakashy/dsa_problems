def largestNumber(A):
    largest = list(map(str, A))

    for i in range(1, len(A)):
        for j in range(len(A) - 1):
            if largest[j] + largest[j+1] < largest[j+1] + largest[j]:
                largest[j], largest[j+1] = largest[j+1], largest[j]


    return 0 if largest[0] == "0" else "".join(largest)

A = [0, 0, 0, 0, 0]
print(largestNumber(A))

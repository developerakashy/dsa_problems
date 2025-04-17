def occurence_of_number(A):

    hash = {}
    A.sort()
    for num in A:
        hash[num] = hash.get(num, 0) + 1

    return list(hash.values())


A = [3,3,3,3,2]
print(occurence_of_number(A))

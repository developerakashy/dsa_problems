A = [0, 1, 2, 3]

def plusOne(A):
    n = len(A)
    string = ''

    for i in range(0, n):
        string += str(A[i])

    string = str(int(string) + 1)

    new_list = []
    for j in range(len(string)):
        new_list.append(int(string[j]))

    return new_list



print(plusOne(A))

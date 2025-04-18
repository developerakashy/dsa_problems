def closest_to_zero(A):
    closest_num = max(A)

    for i in range(len(A)):
        if abs(A[i]) < abs(closest_num):
            closest_num = A[i]

    return closest_num

A = [-4,-2,1,4,8]

print(closest_to_zero(A))

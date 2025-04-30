def rotate(matrix):
    rotations = len(matrix) // 2

    for j in range(rotations):
        i = j
        end = (len(matrix) - 1)

        while i < end - j:
            print(i, j)
            temp_value = matrix[j][i]
            print(temp_value)


            temp_value, matrix[i][end - j] = matrix[i][end - j], temp_value
            print(temp_value)


            temp_value, matrix[end - j][end-i] = matrix[end - j][end-i], temp_value
            print(temp_value)


            temp_value, matrix[end-i][0+j] = matrix[end-i][0+j], temp_value
            print(temp_value)


            matrix[j][i] = temp_value

            i += 1


    return matrix


# Transpose
def easy_approach(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


    for row in matrix:
        row.reverse()

    return matrix





matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# print(rotate(matrix1))
print(easy_approach(matrix1))

# this above function mutate the original matrix

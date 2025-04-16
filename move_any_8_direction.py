# step occurs only for give co-ordinates
A = [-17, -13]
B = [1, -5]

# def move(A, B):
#     step = 0

#     for i in range(len(A) - 1):
#         if A[i] == A[i+1] and ((B[i] + 1 == B[i+1]) or (B[i] - 1 == B[i+1])):
#             step += 1
#         elif ((A[i] + 1 == A[i+1]) or (A[i] - 1 == A[i+1])) and ((B[i] + 1 == B[i+1]) or (B[i] == B[i+1]) or (B[i] - 1 == B[i+1])):
#             step += 1

#     return step

def move(A, B):
    step = 0

    for i in range(1, len(A)):
        dx = abs(A[i] - A[i-1])
        dy = abs(B[i] - B[i-1])
        step += max(dx, dy)

    return step

print(move(A, B))

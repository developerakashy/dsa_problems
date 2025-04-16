# def partitions(A,B):
#     count = 0

#     for i in range(0, A - 2):
#         for j in range(i+1, A-1):
#             for k in range(j+1, j+2):
#                 if sum(B[:i+1]) == sum(B[i+1:j+1]) == sum(B[j+1:]):
#                     print(B[:i+1])
#                     print(B[i+1:j+1])
#                     print(B[j+1:])
#                     print(i,j,k)
#                     count += 1

#     return count

# def partitions(A, B):
#     end = A - 2
#     w = A - 2
#     left = 1
#     count = 0

#     while w > 0:
#         left = 1
#         for i in range(w, end+1):
#             if(sum(B[:left]) == sum(B[left:i+1]) == sum(B[i+1:])):
#                 count += 1
#             left += 1
#         w -= 1

#     return count

def partitions(A, B):
    total = sum(B)
    if total % 3 != 0:
        return 0

    target = total // 3
    suffix = [0] * A
    suffix_sum = 0

    for i in reversed(range(A)):
        suffix_sum += B[i]
        if suffix_sum == target:
            suffix[i] = 1
    print(suffix)

    for i in reversed(range(A - 1)):
        suffix[i] += suffix[i + 1]
    print(suffix)

    prefix_sum = 0
    ways = 0
    for i in range(A - 2):
        prefix_sum += B[i]
        if prefix_sum == target:
            ways += suffix[i + 2]  

    return ways




A = 5
B = [1, 2, 3, 0, 3]

print(partitions(A, B))

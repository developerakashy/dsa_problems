# def flip(s):
#     one_count = s.count('1')

#     n = len(s)
#     if one_count == n:
#         return []

#     temp_s = s
#     max_one_count = 0
#     max_one_count_arr = []
#     for i in range(0, n-1):
#         for j in range(i, n):
#             travel = i
#             while travel <= j:
#                 if (int(temp_s[travel]) == 1):
#                     temp_s = temp_s[:travel] + '0' + temp_s[travel+1:]
#                 else:
#                     temp_s = temp_s[:travel] + '1' + temp_s[travel+1:]

#                 travel += 1

#             temp_one_count = temp_s.count('1')

#             if max_one_count < temp_one_count:
#                 max_one_count = temp_one_count
#                 max_one_count_arr = []
#                 max_one_count_arr.append([i+1, j+1])
#             elif max_one_count == temp_one_count:
#                 max_one_count_arr.append([i+1, j+1])

#             temp_s = s


#     return max_one_count_arr

def flip(A):
    current_sum = 0
    max_sum = 0
    start = 0
    best_range = []

    for i in range(len(A)):
        val = 1 if A[i] == '0' else -1

        current_sum += val

        if current_sum < 0:
            current_sum = 0
            start = i+1
        elif max_sum < current_sum:
            max_sum = current_sum
            best_range = [start+1,i+1]

    return best_range




s = '1101'

print(flip(s))

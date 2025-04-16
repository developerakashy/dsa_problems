def bubble_sort(arr):
    n = len(arr)
    flag = True

    while flag:
        flag = False
        for j in range(1, n):
            if arr[j - 1] > arr[j]:
                flag = True
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

print(bubble_sort([23,12,56,98,2]))

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low+high)/2)

        if target == nums[mid]:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1

nums = [-1,0,3,5,9,12]
target = 8
print(binary_search(nums, target))

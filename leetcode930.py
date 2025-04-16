nums = [0,1,0,1,0]
goal = 2

def numSubArraysWithSum(nums, goal):
    w = len(nums)
    n = len(nums)
    left = 0
    count = 0

    while w >= 0:
        for right in range(w, n):
            if sum(nums[left:right+1:]) == goal:
                count += 1
            left += 1
        left = 0
        w-=1

    return count

print(numSubArraysWithSum(nums, goal))

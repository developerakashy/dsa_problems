def longest_consecutive(nums):
    nums.sort()
    count = 1
    prev = nums[0]

    for num in nums:
        if num == prev + 1:
            count += 1
            prev = num

    return count

A = [100,4,200,1,3,2]

print(longest_consecutive(A))

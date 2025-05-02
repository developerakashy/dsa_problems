def majority(nums):
    num_count = {}
    ele = nums[0]
    count = 1

    for num in nums:
        if num in num_count:
            num_count[num] += 1
        else:
            num_count[num] = 1

        if num_count[num] > count:
            count = num_count[num]
            ele = num

    return ele

nums = [2, 2, 1, 1, 1, 1,1, 2, 2]
print(majority(nums))

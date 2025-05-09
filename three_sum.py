def three_sum(nums):
    nums.sort()
    result = set()

    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    return [list(triplet) for triplet in result]

def optimal(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        curr = nums[i]

        if curr > 0:
            break
        elif i > 0 and nums[i] == nums[i-1]:
            continue

        left = i+1
        right = len(nums) - 1

        while left < right :
            if nums[left] + nums[right] + curr == 0:
                result.append([nums[left], nums[right], curr])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            elif nums[left] + nums[right] + curr < 0:
                left += 1
            else:
                right -= 1


    return result

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
print(optimal(nums))

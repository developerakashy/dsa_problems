def duplicates(nums):
    s = set(nums)

    if len(s) == len(nums):
        return False

    return True


nums = [1, 2, 3, 4]
print(duplicates(nums))

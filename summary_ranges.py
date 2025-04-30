def summary_ranges(nums):
    ranges = []
    start = curr = nums[0]

    for i in range(1, len(nums)):
        if nums[i] == curr + 1:
            curr = nums[i]
            continue

        range_str = str(start) if start == curr else str(start) + "->" + str(curr)


        ranges.append(range_str)
        start = curr = nums[i]

    range_str = str(start) if start == curr else str(start) + "->" + str(curr)

    ranges.append(range_str)


    return ranges

nums = [0,2,3,4,6,7,9]
print(summary_ranges(nums))

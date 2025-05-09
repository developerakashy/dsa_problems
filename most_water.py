def most_water(height):
    max_area = 0

    left = 0
    right = len(height) - 1

    while left < right:
        breadth = right - left
        length = min(height[left], height[right])
        max_area = max(max_area, breadth*length)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

height = [1, 1]
print(most_water(height))

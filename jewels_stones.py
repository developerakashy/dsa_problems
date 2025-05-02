def jewels_stones(jewels, stones):
    count = 0
    jewels_count = {key:1 for key in jewels}

    for stone in stones:
        if jewels_count.get(stone):
            count += 1

    return count

jewels = 'aA'
stones = 'aAAbbbbb'
print(jewels_stones(jewels, stones))

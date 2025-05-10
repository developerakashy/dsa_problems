def daily_temperatures(temperatures):
    result = []

    for i in range(len(temperatures)):
        days = 0
        next_temp = i+1
        warm = False
        while not warm and next_temp < len(temperatures):
            if temperatures[i] < temperatures[next_temp]:
                warm = True

            next_temp += 1
            days += 1

        if warm:
            result.append(days)
        else:
            result.append(0)

    return result

def optimal(temperatures):
    result = [0] * len(temperatures)
    stack = []

    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]:
            result[stack[-1][1]] = i - stack[-1][1]
            stack.pop()

        stack.append([temperatures[i], i])

    return result


temp = [73,74,75,71,69,72,76,73]
print(daily_temperatures(temp))
print(optimal(temp))

def baseball(operations):
    result = []

    for op in operations:
        if op == 'C':
            result.pop()
        elif op == 'D':
            result.append(result[-1]*2)
        elif op == '+':
            result.append(result[-1]+result[-2])
        elif int(op):
            result.append(int(op))

    return sum(result)

ops = ["5","2","C","D","+"]
print(baseball(ops))

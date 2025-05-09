def reverse_polish_notation(tokens):
    result = []

    for op in tokens:
        new_val = None

        if op == '+':
            new_val = result[-2] + result[-1]

        elif op == '-':
            new_val = result[-2] - result[-1]

        elif op == '*':
            new_val = result[-2] * result[-1]

        elif op == '/':
            new_val = int(result[-2] / result[-1])

        else:
            result.append(int(op))

        if new_val != None:
            result.pop()
            result[-1] = new_val

    return result[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(reverse_polish_notation(tokens))

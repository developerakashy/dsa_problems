def valid_parenthesis(s):
    result = []

    for bracket in s:
        if bracket == '(' or bracket == '[' or bracket == '{':
            result.append(bracket)
        elif not result:
            return False
        elif (result[-1]+bracket == '()' or
            result[-1]+bracket == '[]' or
            result[-1]+bracket == "{}"):
            result.pop()
        else:
            return False

    return len(result) == 0

s = "({})" 
print(valid_parenthesis(s))

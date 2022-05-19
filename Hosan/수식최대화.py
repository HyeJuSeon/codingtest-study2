def calculate(expression, pri, depth) :
    if depth == 2 :
        return eval(expression)
    tmp = expression.split(pri[depth])
    result = ""
    for i in range(len(tmp)) :
        result += str(calculate(tmp[i], pri, depth+1))
        if i < len(tmp) -1 :
            result += pri[depth]
    return eval(result)

def solution(expression) :
    result = 0
    pri = [['*', '-', '+'], ['*', '+', '-'], ['+', '*', '-'],  ['+', '-', "*"], ['-', '+', '*'], ['-', '*', '+']]
    for i in range(6) :
        tmp = calculate(expression, pri[i], 0)
        if abs(tmp) > abs(result) :
            result = tmp
    return abs(result)

print(solution(input()))
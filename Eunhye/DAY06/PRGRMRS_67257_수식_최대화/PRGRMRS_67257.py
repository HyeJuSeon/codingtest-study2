from itertools import permutations
from collections import deque

def divide(s):
    operator = "*+-"
    operands = []
    operators = []
    idx = -1
    for i in range(len(s)):
        if s[i] in operator:
            operands.append(int(s[idx+1:i]))
            operators.append(s[i])
            idx = i
    
    operands.append(int(s[idx+1:]))
    return operands, operators

def solution(expression):
    answer = 0
    operands, operators = divide(expression)
    permu = [p for p in permutations(set(operators))]
    
    for p in permu:
        stack1 = []
        stack2 = []
        rands = deque(operands)
        rators = deque(operators)
        for curr in p:
            rands.reverse()
            rators.reverse()
            stack1.append(rands.pop())

            for _ in range(len(rators)):

                stack1.append(rands.pop())
                rator = rators.pop()
                if rator == curr:

                    other_num = stack1.pop() 
                    new_num = stack1.pop()

                    if curr == "*":
                        new_num *= other_num
                    elif curr == "+":
                        new_num += other_num
                    else:
                        new_num -= other_num
                    stack1.append(new_num)

                else:
                    stack2.append(rator)
            rands = deque(stack1)
            rators = deque(stack2)
            stack1 = []
            stack2 = []

        answer = max(answer, abs(rands[0]))
    return answer
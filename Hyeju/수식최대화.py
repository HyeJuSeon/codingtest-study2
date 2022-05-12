from itertools import permutations
import re
def solution(expression):
    ans = 0
    cases = permutations(['+', '-', '*'], 3)
    for case in cases:
        ans = max(ans, abs(calc(case, expression)))
    return ans

def calc(ops, exp):
    exp = re.split('([-|+|*])', exp)
    for op in ops:
        s = []
        while exp:
            tmp = exp.pop(0)
            if tmp == op:
                s.append(str(eval(s.pop() + op + exp.pop(0))))
            else:
                s.append(tmp)
        exp = s
    return int(exp[-1])

# print(solution("100-200*300-500+20"))
# print(solution("50*6-3*2"))

#  가장 큰 숫자를 제출하는 것
# 계산된 결과가 음수라면 해당 숫자의 절댓값으로 변환하여 제출
expression = "100-200*300-500+20"

import re
def solution(expression):
    answer = []
    combinations = [['+','-','*'],['+','*','-'],['-','+','*'],['-','*','+'],['*','-','+'],['*','+','-']]
    for combination in combinations:
        operand = re.split('[*+-]',expression)
        operator = re.split('[0-9]+',expression)[1:-1]
        print(operand)
        print(operator)
        for comb in combination:
            while comb in operator:
                idx = operator.index(comb)
                operand[idx] = str(eval(operand[idx] + comb + operand[idx+1]))
                del operand[idx+1]
                del operator[idx]
        answer.append(abs(int(operand[0])))

    return max(answer)



solution(expression)
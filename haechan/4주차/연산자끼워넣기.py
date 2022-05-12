from itertools import permutations

n = int(input())
num_list = list(map(int, input().split()))
oper_list = list(map(int, input().split()))
o = ['+', '-', '*', '/']
operators = []

for i, oper in enumerate(oper_list):
    for _ in range(oper):
        operators.append(o[i])

result_list = []
for op_list in set(permutations(operators, len(operators))):
    result_num = num_list[0]
    for i in range(len(op_list)):
        if op_list[i] == '+':
            result_num += num_list[i+1]
        elif op_list[i] == '-':
            result_num -= num_list[i+1]
        elif op_list[i] == '*':
            result_num *= num_list[i+1]
        else:
            if result_num < 0:
                result_num = -(abs(result_num) // num_list[i+1])
            else:
                result_num = result_num // num_list[i+1]
    result_list.append(result_num)

print(max(result_list))
print(min(result_list))
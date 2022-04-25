#dfs
N = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1e9
min_value = 1e9

def dfs(i, arr):
    global add, sub, mul, div, max_value, min_value

    if i == N:
        max_value = max(max_value, arr)
        min_value = min(min_value, arr)

    else:
        if add > 0:
            add -= 1
            dfs(i+1,arr + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, arr - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, arr * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, int(arr / data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)


'''
from collections import deque
from itertools import permutations
#식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 
#나눗셈은 정수 나눗셈으로 몫만 취한다. 

N = int(input())
A = list(map(int,input().split()))
oper = list(map(int,input().split()))
oper = list(oper[0]*'+')+list(oper[1]*'-')+list(oper[2]*'*')+list(oper[3]*'/')
case = list(permutations(oper))
result_min = 9999999999999999999
result_max = 0

for c in case:
    dq = deque(A)
    first_num = dq.popleft()
    result = first_num
    dq_o = deque(c)
    while dq_o:
        o = dq_o.popleft()
        if o == "+":
            result += dq.popleft()
        elif o == "-":
            result -= dq.popleft()
        elif o == "*":
            result *= dq.popleft()
        elif o == "/":
            result = int(result / dq.popleft())
    
    result_min = min(result_min, result)
    result_max = max(result_max, result)

print(result_max)
print(result_min)
'''

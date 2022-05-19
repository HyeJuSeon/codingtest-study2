'''1부터 n을 만드는 방법으로..?'''

from collections import deque

def bfs(n):
    dq = deque()
    dq.append((1, [1])) # n, n연산 기록
    checked = [0] * (n+1) # 해당 숫자에 대한 최초 연산여부를 기록해두고, 그 뒤에 일어나는 연산은 안하기 위해

    while dq:
        x, x_list = dq.popleft()
        
        for nx in [x+1, x*2, x*3]:
            if nx <= n and not checked[nx]:
                if nx == n:
                    return x_list + [nx]
                dq.append((nx, x_list + [nx]))
                checked[nx] = 1


n = int(input())
if n == 1:
    print(0)
    print(1)
else:
    case = bfs(n)
    print(len(case)-1)
    print(" ".join(map(str, case[::-1])))
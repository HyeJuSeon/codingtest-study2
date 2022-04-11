## 풀이

## 코드

```
import sys
from collections import deque

#D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다. 
# 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
def D(n):
    result = n*2
    if result > 9999:
        return result % 10000
    return result

# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다. 
# n이 0 이라면 9999 가 대신 레지스터에 저장된다.
def S(n):
    result = n-1
    if n==0:
        return 9999
    return result

# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
#  이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
def L(n):
    d1 = n//1000
    d2 = (n//100)%10
    d3 = (n//10)%10
    d4 = n%10
    result = ((d2*10+d3)*10+d4)*10+d1
    return result

# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
#  이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
def R(n):
    d1 = n//1000
    d2 = (n//100)%10
    d3 = (n//10)%10
    d4 = n%10
    result = ((d4*10+d1)*10+d2)*10+d3
    return result

def go(s, t):
    queue = deque()
    visited = set()
    queue.append((s,""))
    visited.add(s)
    while queue:
        cur_num, oper = queue.popleft()
        if cur_num == t:
            print(oper)
            return
        
        tmp_D = D(cur_num)
        if tmp_D not in visited:
            visited.add(tmp_D)
            queue.append((tmp_D,oper+"D"))
        tmp_S = S(cur_num)
        if tmp_S not in visited:
            visited.add(tmp_S)
            queue.append((tmp_S,oper+"S"))
        tmp_L = L(cur_num)
        if tmp_L not in visited:
            visited.add(tmp_L)
            queue.append((tmp_L,oper+"L"))
        tmp_R = R(cur_num)
        if tmp_R not in visited:
            visited.add(tmp_R)
            queue.append((tmp_R,oper+"R"))

T = int(sys.stdin.readline())

for _ in range(T):
    start, target = map(int,sys.stdin.readline().strip().split())
    go(start, target)
```








## 풀이

## 코드

```python
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
  A, B = input().rstrip().split()
  result = ""
  dq = deque([(A, "")])
  visited = [ 0 for _ in range(10000)]
  while dq:
    src, cmd = dq.popleft()
    if src == B:
      result = cmd if len(result) > len(cmd) or not result else result
    elif not result or (result and len(cmd) < len(result)):
      if len(src) < 4:
        src = "0"*(4-len(src)) + src
      D, S, L, R = int(src)*2%10000, int(src)-1 if int(src) > 0 else 9999, int(src[1:]+src[0]), int(src[3]+src[:3])
      if not visited[D]:
        dq.append((str(D), cmd+"D"))
        visited[D] = 1
      if not visited[S]:
        dq.append((str(S), cmd+"S"))
        visited[S] = 1
      if not visited[L]:
        dq.append((str(L), cmd+"L"))
        visited[L] = 1
      if not visited[R]:
        dq.append((str(R), cmd+"R"))
        visited[R] = 1
  print(result)
```

import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque([[N]])
ans = []

while q:
    arr = q.popleft()
    n = arr[-1]
    if n == 1:
        ans = arr
        break

    if n % 3 == 0:
        q.append(arr + [n // 3])
    if n % 2 == 0:
        q.append(arr + [n // 2])
    q.append(arr + [n - 1])

print(len(ans) - 1)
print(*ans)

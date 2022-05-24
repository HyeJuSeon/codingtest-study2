## 풀이

## 코드

```python
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
result = 0

for _ in range(K):
  r, c = map(int, input().split())
  graph[r-1][c-1] = 1

for i in range(N):
  for j in range(M):
    if graph[i][j] and not visited[i][j]:
      queue = deque([(i, j)])
      visited[i][j] = 1
      cnt = 0

      while queue:
        y, x = queue.popleft()
        cnt += 1
        for k in range(4):
          ny, nx = y + dy[k], x + dx[k]
          if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] and not visited[ny][nx]:
            visited[ny][nx] = 1
            queue.append((ny, nx))

      result = max(result, cnt)

print(result)
```

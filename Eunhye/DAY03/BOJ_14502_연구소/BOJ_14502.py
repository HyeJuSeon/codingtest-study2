from collections import deque
import copy

def bfs():
  global result
  cnt = len(empty) - 3
  data = copy.deepcopy(graph)
  queue = deque(virus)
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if 0 <= ny < N and 0 <= nx < M and data[ny][nx] == 0:
        queue.append((ny, nx))
        data[ny][nx] = 2
        cnt -= 1

  result = max(result, cnt)

def dfs(cnt):
  if cnt == 3:
    bfs()
    return
  for i in range(N):
    for j in range(M):
      if graph[i][j] == 0:
        graph[i][j] = 1
        dfs(cnt+1)
        graph[i][j] = 0

N, M = map(int, input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

graph = [list(map(int, input().split())) for _ in range(N)]
result = 0
empty = []
virus = []
for i in range(N):
  for j in range(M):
    if not graph[i][j]:
      empty.append((i, j))
    elif graph[i][j] == 2:
      virus.append((i, j))
      
dfs(0)
print(result)
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
cache = [[0 for _ in range(N)] for _ in range(N)]

cache[0][0] = 1
for i in range(N):
  for j in range(N):
    jump = graph[i][j]
    if not cache[i][j] or not jump:
      continue
    if i + jump < N:
      cache[i+jump][j] += cache[i][j]
    if j + jump < N:
      cache[i][j+jump] += cache[i][j]
print(cache[N-1][N-1])
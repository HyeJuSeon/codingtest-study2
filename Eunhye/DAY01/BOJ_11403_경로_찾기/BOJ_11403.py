# 플로이드 와샬(Floyd Warshall)

N = int(input())

adj = [ list(map(int, input().split())) for _ in range(N)]

for k in range(N): # k는 거쳐가는 노드
  for i in range(N): # i는 출발 노드
    if adj[i][k]:
      for j in range(N): # j는 도착 노드
        if adj[k][j]:
          adj[i][j] = 1

for idx in range(N):
  print(*adj[idx], sep=" ") 
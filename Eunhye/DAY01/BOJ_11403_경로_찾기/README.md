## 풀이

플로이드 와샬(Floyd Warshall) 알고리즘을 이용해 풀어주었습니다.

i에서 k를 거쳐 j까지 갈 수 있다면 adj\[i]\[j]는 도달 할 수 있으므로 1로 처리해주었습니다.

## 코드

```python
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
```

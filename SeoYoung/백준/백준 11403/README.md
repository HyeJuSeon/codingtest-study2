## 백준 11403 경로찾기

### 알고리즘

```txt
 ✅ DFS
```

### 코드 구현

사용 언어 : **파이썬**

```python
def dfs(graph, v, visited):
    for i in range(len(graph)):
        # v->i로 가는 경로가 있고 i를 방문한 적이 없으면
        # i를 방문 처리한 후 dfs 탐색 (i->다른 노드)
        # i->다른 노드의 경로가 있다면 v->다른 노드가 가능한 것이므로 visited[다른 노드]=1로 처리 가능
        if graph[v][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(graph, i, visited)

N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    visited=[0]*N
    dfs(graph,i,visited)
    print(*visited)
```

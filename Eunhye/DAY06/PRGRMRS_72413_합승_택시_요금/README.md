## 풀이

## 코드

```python
from heapq import heappop, heappush
INF = 9876543210
def dijkstra(src, adj):
    src_lst = [INF for _ in range(len(adj)+1)]
    # 자기 자신 제외
    src_lst[src] = 0
    # 출발 노드 설정
    hq = [[src, 0]]
    while hq:
        # print(hq)
        v, fee = heappop(hq)
        for v2, fee2 in adj[v]:
            fee2 += fee
            if src_lst[v2] > fee2:
                src_lst[v2] = fee2
                heappush(hq, [v2, fee2])
    return src_lst


def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n+1)]
    for f in fares:
        # 인접 리스트가 더 효율적
        adj[f[0]].append([f[1], f[2]])
        adj[f[1]].append([f[0], f[2]])

    answer = INF
    for i in range(1, n+1):
        # i 에서 출발하는 최소비용 리스트
        dist = dijkstra(i, adj)
        # 출발점인 s에서 출발하여 i까지 합승, 그리고 각각 a, b로 가는 비용을 모두 더해주면 된다
        # 간선이 양방향이기 때문에 한번만 호출 가능
        # ex) s에서 i로 가는 것과 i에서 s로 가는 최소비용이 같음
        ans = dist[s] + dist[a] + dist[b]
        if answer > ans:
            answer = ans
    return answer
```

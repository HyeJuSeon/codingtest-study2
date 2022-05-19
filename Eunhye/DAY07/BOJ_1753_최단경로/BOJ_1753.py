from collections import defaultdict
from heapq import heappop, heappush
from math import inf
import sys
input = sys.stdin.readline
def dijkstra(src, adj, V):
    dist = [inf for _ in range(V+1)]
    hq = [[0, src]]
    dist[src] = 0
    while hq:
        w, v = heappop(hq)
        if w > dist[v]:
            continue
        for nw, nv in adj[v]:
            nw += w
            if dist[nv] > nw:
                dist[nv] = nw
                heappush(hq, (nw, nv))
    return dist

V, E = map(int, input().split())
src = int(input())
adj = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    heappush(adj[u], (w, v))
dist = dijkstra(src, adj, V)
for i in range(1,V+1):
    if dist[i] == inf:
        print("INF")
    else:
        print(dist[i])
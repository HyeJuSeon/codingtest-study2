import sys
from math import inf
import heapq

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
arr = [[] for _ in range(V + 1)]
visit = [0 for _ in range(V + 1)]
dist = [inf for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    arr[a].append((c, b))

pq = [(0, K)]
dist[K] = 0
while pq:
    curr_e, curr_v = heapq.heappop(pq)
    if visit[curr_v]:
        continue
    visit[curr_v] = 1
    for next_dist, next in arr[curr_v]:
        next_dist += curr_e
        if dist[next] > next_dist:
            dist[next] = next_dist
            heapq.heappush(pq, (next_dist, next))

for d in dist[1:]:
    if d == inf:
        print("INF")
    else:
        print(d)
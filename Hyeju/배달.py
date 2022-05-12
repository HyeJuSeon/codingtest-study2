from queue import PriorityQueue
from math import inf

def solution(N, road, K):
    dist = [inf] * (N + 1)
    visit = [0] * (N + 1)
    # arr = [] * (N + 1) # ???
    arr = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        arr[a].append([c, b])
        arr[b].append([c, a])
    # dijkstra
    pq = PriorityQueue()
    pq.put([0, 1])
    dist[1] = 0
    while not pq.empty():
        w, n = pq.get()
        if visit[n]: continue
        visit[n] = 1
        for i in range(len(arr[n])):
            next = arr[n][i][1]
            next_dist = w + arr[n][i][0]
            if dist[next] > next_dist:
                dist[next] = next_dist
                pq.put([next_dist, next])
    ans = [d for d in dist[1:] if d <= K]
    return len(ans)

# print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
# print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))

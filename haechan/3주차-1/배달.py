import heapq, math

# 해당 노드까지 갈 수 있는 최단 시간(거리)을 구하고, distance리스트에 최단 시간을 기록
def dikjstra(start, distance, graph):
    q = []
    heapq.heappush(q, (0, start)) # 우선순위 큐
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 새로 구한 거리가 기존에 기록된 거리보다 크다면 버림
            continue
        for i in graph[now]: # i[0] -> 도착 노드, i[1] -> 소요 시간(거리)
            new_dist = dist + i[1]
            if new_dist < distance[i[0]]: # 현재 기록된 거리보다 새로운 거리가 더 짧으면 새로 갱신
                distance[i[0]] = new_dist
                heapq.heappush(q, (new_dist, i[0]))

def solution(N, road, K):
    result = 0
    distance = [math.inf] * (N+1) # 0번째는 버리는 인덱스
    distance[1] = 0 # 1번 마을부터 시작하므로 1에서 1까지의 거리는 0
    
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))

    dikjstra(1, distance, graph)
    
    for dist in distance[1:]:
        if dist <= K: # 최단시간이 K시간보다 같거나 작을때
            result += 1 # 해당 마을까지 갈 수 있다면 +1
    
    return result
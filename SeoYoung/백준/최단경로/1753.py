import sys 
import heapq 

# 이 2개 처리 안해주면 시간 초과 에러남
input = sys.stdin.readline 
INF = sys.maxsize

# 정점 개수 V, 간선 개수 E
V,E=map(int,input().split())
# 시작 정점의 번호
K=int(input())
info=[list(map(int,input().split())) for _ in range(E)]
graph=[[] for _ in range(V+1)]

for u,v,w in info:
    graph[u].append((w,v))

dist=[INF]*(V+1)
dist[K]=0
heap=[]
heapq.heappush(heap, (0,K))

while heap:
    # K-destination : 현재까지의 최소 거리 value
    value, destination=heapq.heappop(heap)

    # destination-d의 직선 거리
    for v,d in graph[destination]:
        next_value=value+v

        if next_value<dist[d]:
            dist[d]=next_value
            heapq.heappush(heap, (next_value, d))

for i in range(1,V+1):
    if dist[i]==INF:
        print('INF')
    else:
        print(dist[i])

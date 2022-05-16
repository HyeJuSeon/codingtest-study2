import heapq
INF=int(1e9)

def solution(n, s, a, b, fares):
    graph=[[] for _ in range(n+1)]
    
    for x,y,z in fares:
        graph[x].append((z,y))
        graph[y].append((z,x))
    
        
    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start]=0
        heap=[]
        # (start에서 특정지점 d까지의 최단거리, 특정지점 d) 형태로 heap에 삽입됨
        heapq.heappush(heap,(0,start))
        
        while heap:
            # start-destination: 현재까지의 최소 value
            value,destination=heapq.heappop(heap)
            
            # destination-d의 직선거리 v
            for v,d in graph[destination]:
                next_value=value+v
                
                if next_value<dist[d]:
                    dist[d]=next_value
                    heapq.heappush(heap,(next_value,d))
        
        return dist
    
    dp=[[]]+[dijkstra(i) for i in range(1,n+1)]
    
    answer=INF
    for i in range(1,n+1):
        answer=min(dp[i][a]+dp[i][b]+dp[i][s], answer)
    
    return answer
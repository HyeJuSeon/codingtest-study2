# 플로이드 워셜로 풀었으나 실패,,
# 다익스트라로 풀어야 함
import math

INF=math.inf
V,E=map(int,input().split())
K=int(input())
info=[list(map(int,input().split())) for _ in range(E)]
graph=[[INF]*(V+1) for _ in range(V+1)]

for u,v,w in info:
    graph[u][v]=w

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if graph[i][k]+graph[k][j]<graph[i][j]:
                graph[i][j]=graph[i][k]+graph[k][j]

for i in range(1,V+1):
    if graph[K][i]==INF:
        if K==i: 
            print(0)
        else:
            print("INF")
    else:
        print(graph[K][i])


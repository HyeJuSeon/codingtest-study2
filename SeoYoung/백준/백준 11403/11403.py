# 가중치 없는 방향 그래프 G 
# 모든 정점 (i,j)에 대해서 
# i에서 j로 가는 경로가 있는지 없는지 구하는 프로그램을 작성

def dfs(graph, v, visited):

    for i in range(len(graph)):
        if graph[v][i]==1 and visited[i]==0:
            visited[i]=1
            dfs(graph, i, visited)

N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    visited=[0]*N
    dfs(graph,i,visited)
    print(*visited)
    

    

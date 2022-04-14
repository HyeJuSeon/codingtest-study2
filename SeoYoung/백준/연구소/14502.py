from collections import deque
import copy
import sys

input=sys.stdin.readline

dx=[-1,1,0,0]
dy=[0,0,-1,1]

n,m=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(n)]
answer=0

def bfs(i,j,graph):
    q=deque()
    q.append((i,j))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                q.append((nx,ny))
                graph[nx][ny]=2


def makeWall(cnt):
    global answer
    if cnt==3:
        copy_graph=copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                if graph[i][j]==2:
                    bfs(i,j,copy_graph)
        answer=max(answer,sum(copy_graph,[]).count(0))
        return 
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j]==0:
                    graph[i][j]=1
                    makeWall(cnt+1)
                    graph[i][j]=0


makeWall(0)
print(answer)

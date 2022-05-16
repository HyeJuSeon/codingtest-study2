from collections import deque

def solution(maps):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
    h=len(maps)
    w=len(maps[0])
    
    graph=[[-1 for _ in range(w)] for _ in range(h)]
    
    q=deque()
    q.append([0,0])
    
    graph[0][0]=1
    
    while q:
        y,x=q.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            
            if 0<=nx<w and 0<=ny<h and maps[ny][nx]==1:
                if graph[ny][nx]==-1:
                    graph[ny][nx]=graph[y][x]+1
                    q.append([ny,nx])

    answer=graph[-1][-1]
    return answer
from collections import deque
n,m,k = map(int, input().split())

graph = [[0] * (m+1) for i in range(n+1)]
visited = [[0] * (m+1) for _ in range(n+1)]
trash = 0

for i in range(k):
    r,c = map(int,input().split())
    graph[r][c] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

dq = deque()

def bfs(x,y):
    global trash
    dq.append([x,y])
    visited[x][y] = 1
    trash += 1

    while dq:
        x, y = dq[0][0], dq[0][1]
        dq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= n and 0 <= ny <= m and visited[nx][ny] == 0 and graph[nx][ny] == 1:
                dq.append([nx,ny])
                visited[nx][ny] = 1
                trash += 1

result = 0

for x in range(n+1):
    for y in range(m+1):
        if graph[x][y] == 1:
            bfs(x,y)
            result = max(result,trash)
            trash = 0

print(result)
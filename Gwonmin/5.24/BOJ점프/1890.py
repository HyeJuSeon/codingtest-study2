#dp
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for y in range(n):
    for x in range(n):
        if y == n-1 and x == n-1:
            break
        if dp[y][x]>=1:
            dy = y+arr[y][x]
            dx = x+arr[y][x]
            if 0<=dy<n:
                dp[dy][x] += dp[y][x]
            if 0<=dx<n:
                dp[y][dx] += dp[y][x]

print(dp[-1][-1])






'''
from collections import deque
n = int(input())
graph = [list(map(int,input().split())) for i in range(n)]
visited = [[0]*n for _ in range(n)]
route = 0

dx = [1,0]
dy = [0,1]

dq = deque()

def bfs(x,y):
    global route
    dq.append([x,y])
    visited[x][y] += 1

    while dq:
        x, y = dq[0][0], dq[0][1]
        # print(*visited, sep='\n')
        # print(dq)
        # print('--------')
        dq.popleft()
        for i in range(2):
            if graph[x][y] == 0:
                continue

            nx = x + dx[i]*graph[x][y]
            ny = y + dy[i]*graph[x][y]
            if 0 <= nx < n and 0 <= ny < n :
                dq.append([nx,ny])
                visited[nx][ny] += 1
                if nx == n-1 and ny == n-1:
                    route += 1
                    graph[n-1][n-1] += 1

bfs(0,0)
print(route)

'''










'''
시간초과

n = int(input())
graph = [list(map(int,input().split())) for i in range(n)]
count = 0

def go(pos):
    global count
    if pos == [n-1,n-1]:
        count += 1
        return

    num = graph[pos[0]][pos[1]]
    if num == 0:
        return

    if pos[0]+num < n:
        go([pos[0]+num, pos[1]])

    if pos[1]+num < n:
        go([pos[0], pos[1]+num])

    return

go([0,0])
print(count)
'''

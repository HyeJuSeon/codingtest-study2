import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
dx = [0, 0, 1, -1]
dy = [1, -1, 0 ,0]

def dfs(x, y) :
    visited[x][y] = 1
    global result
    if field[x][y] == 1 :
        result += 1
    for i in range(4) :
        mx = x + dx[i]
        my = y + dy[i]
        if mx > 0 and mx <= height and my > 0 and my <= width :
            if field[mx][my] == 1 and visited[mx][my] == 0 :
                dfs(mx, my)
    return
height, width, N = list(map(int, input().split()))
field = [[0 for _ in range(width+1)] for _ in range(height+1)]
visited = [[0 for _ in range(width+1)] for _ in range(height+1)]
trash = 0
result = 0
for _ in range(N) :
    x, y = list(map(int, input().split()))
    field[x][y] = 1
for i in range(1, height+1) :
    for j in range(1, width+1) :
        result = 0
        if visited[i][j] == 0 :
            dfs(i, j)
            if result > trash :
                trash = result
print(trash)
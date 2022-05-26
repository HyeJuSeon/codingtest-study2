import sys
sys.setrecursionlimit(10**8)
N, M, K = map(int, sys.stdin.readline().split())
mat = [[0] * M for _ in range(N)]
visit = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, sys.stdin.readline().split())
    mat[r - 1][c - 1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
cnt = 0
def dfs(x, y):
    global cnt
    visit[x][y] = 1
    cnt += 1
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < M and mat[a][b] and not visit[a][b]:
            dfs(a, b)

for i in range(N):
    for j in range(M):
        if mat[i][j] and not visit[i][j]:
            cnt = 0
            dfs(i, j)
            ans = max(ans, cnt)
print(ans)

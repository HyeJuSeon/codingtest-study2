import sys

N = int(sys.stdin.readline())
Map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
ans = 0

def dfs(i, j, pipe):
    global ans
    if i == N - 1 and j == N - 1:
        ans += 1
        return

    if pipe == 0 or pipe == 2:
        if j + 1 < N and not Map[i][j + 1]:
            dfs(i, j + 1, 0)
    if pipe == 1 or pipe == 2:
        if i + 1 < N and not Map[i + 1][j]:
            dfs(i + 1, j, 1)
    if i + 1 < N and j + 1 < N:
        if not Map[i + 1][j] and not Map[i][j + 1] and not Map[i + 1][j + 1]:
            dfs(i + 1, j + 1, 2)

dfs(0, 1, 0)
print(ans)

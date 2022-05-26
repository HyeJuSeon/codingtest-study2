import sys

N = int(sys.stdin.readline())
mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            print(dp[N - 1][N - 1])
        d = mat[i][j]
        if i + d < N:
            dp[i + d][j] += dp[i][j]
        if j + d < N:
            dp[i][j + d] += dp[i][j]
            
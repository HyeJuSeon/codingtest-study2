import sys

N = int(sys.stdin.readline())
a = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N - 1, -1, -1):
    next = i + a[i][0]
    if next > N:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], a[i][1] + dp[next])
print(dp[0])

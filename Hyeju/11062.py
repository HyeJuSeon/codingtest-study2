import sys

def sol(i, j):
    turn = (N - (i - j)) % 2
    if i > j:
        return 0
    if dp[i][j]:
        return dp[i][j]
    if i == j:
        if turn:
            return cards[i]
        return 0
    if turn:
        ret = max(sol(i + 1, j) + cards[i], sol(i, j - 1) + cards[j])
    else:
        ret = min(sol(i + 1, j), sol(i, j - 1))
    return ret

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    print(sol(0, N - 1))
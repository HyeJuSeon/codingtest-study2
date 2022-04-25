import sys

def sol(i, j):
    if i > j:
        return 0
    if dp[i][j]:
        return dp[i][j]
    if i == j:
        return cards[i]
    curr = cards[i] + min(sol(i + 2, j), sol(i + 1, j - 1))
    curr = max(curr, cards[j] + min(sol(i, j - 2), sol(i + 1, j - 1)))
    return curr

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cards = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    print(sol(0, N - 1))